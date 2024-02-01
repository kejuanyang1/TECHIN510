# TECHIN 510 LAB 3
### TODO List Application

## Getting Started
Open the terminal and run the following commands:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Activte the envrionment:
```
source .venv/bin/activate
```
If you want to run the app locally:
```
streamlit run app.py
```

## What's Included
- `app.py`: Contains the Streamlit application logic, responsible for rendering the user interface and handling user interactions. 
- `object.py`: Defines the core data structures and database interactions for the Todo List application.
- `README.md`: The markdown file providing a descriptive overview of the project, setup instructions, and additional information.
- `requirements.txt`: A text file listing the Python dependencies for the project, which can be installed using `pip`.

## Lessons Learned
- I learned how to design the schema of database, especially in terms of ensuring flexibility for future enhancements. 
- Moreover, I praticed how to implement create, read, and update functions in todo list application using SQL queries.

## Questions
- I use checkbox element to display the `is_done` state of a todo item. However, I found that only after I clicked it twice, the display would change. I'm not sure why it happens. 