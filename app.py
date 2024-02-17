import streamlit as st
from dotenv import load_dotenv
import os
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.readers.file import PDFReader
from tempfile import NamedTemporaryFile

load_dotenv()

def main():
    st.set_page_config(
        page_title="AI Resume",
        page_icon="📄",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )
    
    if "messages" not in st.session_state.keys():  # Initialize the chat messages history
        st.session_state.messages = [
            {"role": "assistant", "content": "Ask me a question about your resume!"}
        ]

    st.title("AI Resume Bot 🤖📄")
    st.write("Upload your resume or cover letter to get instant feedback.")

    uploaded_file = st.file_uploader("Upload your Resume or Cover Letter", type=["pdf", "docx", "txt"])

    if uploaded_file:
        file_type = uploaded_file.type
        bytes_data = uploaded_file.read()
        with NamedTemporaryFile(delete=False, suffix=f".{file_type.split('/')[-1]}") as tmp:
            tmp.write(bytes_data)

            reader = PDFReader()
            docs = reader.load_data(tmp.name)
            llm = OpenAI(
                model="gpt-3.5-turbo",
                temperature=0.0,
                system_prompt="You are an expert on the content of the document, provide detailed answers to the questions. Use the document to support your answers.",
            )
            index = VectorStoreIndex.from_documents(docs)
        
        os.remove(tmp.name)  # remove temp file after processing

        if "chat_engine" not in st.session_state.keys():  # Initialize the chat engine
            st.session_state.chat_engine = index.as_chat_engine(
                chat_mode="condense_question", verbose=False, llm=llm
            )
        else:
            st.write("Please upload a file to get feedback.")


    if prompt := st.chat_input(
        "Your question"
    ):  # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:  # Display the prior chat messages
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from assistant, generate a new response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chat_engine.stream_chat(prompt)
                st.write_stream(response.response_gen)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message)  # Add response to message history


if __name__ == "__main__":
    main()
