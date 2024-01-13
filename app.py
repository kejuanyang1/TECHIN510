import streamlit as st

def main():
    st.title("Kejuan Yang's Website")

    # Columns for About Section and Profile Picture
    col1, col2 = st.columns(2)

    # About Section in the left column
    with col1:
        st.header("About")
        st.write("Hi there! My name is Kejuan Yang. I am currently pursuing my dual-degree master's in Computer Science at the University of Washington, in collaboration with Tsinghua University, where I specialize in Natural Language Processing and Machine Learning. ")
        st.write("I have a keen interest in agent-driven AI, as I have worked as research assistant in Large Language Model Evaluation. Feel free to connect with me for any collaborative opportunities or just to exchange insights about the world of AI!")
    # Profile Picture in the right column
    with col2:
        for _ in range(5):
            st.write("")

        st.image("imgs/profile.JPG", width=280)
        
        
    # Education Section
    st.header("Education")
    
    st.markdown("""
    #### University of Washington
    **M.S. in Computer Science, Global Innovation eXchange**  
    **GPA:** 4.0/4.0  
    **Duration:** Sep 2023 - Mar 2025
    """, unsafe_allow_html=True)

    st.markdown("""
    #### Tsinghua University
    **M.S. in Data Science and Information Technology, Global Innovation eXchange**  
    **GPA:** 3.87/4.0  
    **Duration:** Sep 2022 - Mar 2025
    """, unsafe_allow_html=True)

    st.markdown("""
    #### Beijing Institute of Technology
    **Bachelor’s in Automation**  
    **GPA:** 90/100  
    **Duration:** Sep 2018 - Jun 2022
    """, unsafe_allow_html=True)

    # Work Experience Section
    st.header("Work Experience")

    # ZhipuAI
    st.markdown("""
    #### ZhipuAI Co., China
    **Position:** Research Assistant, ChatGLM Large Language Model  
    **Duration:** Mar 2023 - Aug 2023  
    - Researched innovative applications of LLM in web browsing tasks like ticketing and online shopping.
    - Developed a web application supporting user instruction in Python, integrating with LLM for action planning.
    - Designed a visual interface for task execution, service logic for web content interaction, and benchmarking tools.
    """, unsafe_allow_html=True)

    # BIGAI
    st.markdown("""
    #### Beijing Institute of General Artificial Intelligence, China
    **Position:** Research Assistant, Multiagent  
    **Duration:** Oct 2021 - Jun 2022
    - Developed a simulation platform for robotic manipulation and interaction using C# and Unity3D.
    - Implemented algorithms for articulated container control and obstacle-avoidance path planning.
    - Integrated VR interaction for first-view object interaction, supporting the BigScene project.
    """, unsafe_allow_html=True)

    # Interests Section
    st.header("Interests")
    st.write("I love badminton, guitar and science fiction movies. Feel free to join me if you share the same interests!")

    # Projects Section
    st.header("Projects")
    st.markdown("""
    #### National Computer Games Competition - International Checkers 64 Squares
    **Date:** Aug 2021  
    **Description:**  
    - Won National Champion
    - Developed a chess-playing program using C++ with advanced search algorithms like Alpha-Beta pruning and Principal Variation Search.
    - Enhanced decision-making efficiency during gameplay through multithreading, evaluating chess positions, moves, and strategies.
    """, unsafe_allow_html=True)

    st.markdown("""
    #### Campus Library User Management Application
    **Date:** Jun 2021  
    **Description:**  
    - Built a user registration and login interface utilizing Vue.js and established communication with the backend database.
    - Successfully deployed the application across the school, achieving over 2000 users.
    """, unsafe_allow_html=True)

    st.markdown("""
    #### National Robocup Competition in 3D Recognition
    **Date:** Nov 2020  
    **Description:**  
    - Won National First Prize
    - Developed a recognition application within the ROS framework, facilitating message transmission and retrieval.
    - Implemented real-time detection and localization of daily objects with a 91% accuracy rate using the YOLOv3 algorithm.
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
