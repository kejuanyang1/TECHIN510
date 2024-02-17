# TECHIN 510 LAB 6
AI Resume Bot

## Getting Started
Open the terminal and run the following commands:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Then activte the envrionment:
```
source .venv/bin/activate
```
If you want to run the app locally:
```
streamlit run app.py
```

## What's Included
- ```app.py```: The main streamlit application
- `README.md`: The markdown file providing a descriptive overview of the project, setup instructions, and additional information.
- `requirements.txt`: A text file listing the Python dependencies for the project, which can be installed using `pip`.

<img src="imgs/example_chat.png" width="650">


## Lessons Learned
- I learned and practiced how to build and host a llm application using chat elemnets from streamlit.
- I practiced how to use Streamlit session states to store and display the dynamic messages.

## Questions (Solved)
- I encountered session not initialized error when I forgot to initialize the chat history session. 
