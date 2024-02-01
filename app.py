import streamlit as st
from datetime import datetime
from dateutil.parser import parse
from pydantic import ValidationError
from object import Todo, init_db, add_todo, get_todos, update_task_completion

def display_todos():
    todos = get_todos()
    for todo in todos:
        todo_id, name, description, created_at, created_by, category, is_done = todo
        
        created_at = parse(created_at) if created_at else datetime.now()

        st.markdown(f"""
        - **Name:** {name}
        - **Description:** {description}
        - **Created At:** {created_at.strftime('%Y-%m-%d %H:%M:%S')}
        - **Created By:** {created_by}
        - **Category:** {category}
        """, unsafe_allow_html=True)

        # Use a separate variable to hold the checkbox value
        checkbox_value = st.checkbox('Done', key=todo_id, value=is_done)
        
        # Update the task completion based on the checkbox value
        update_task_completion(todo_id, checkbox_value)
            
def main():
    init_db()
    st.title("Todo List App")

    with st.form(key='todo_form'):
        name = st.text_input("Name")
        description = st.text_area("Description")
        created_at = datetime.now()
        created_by = st.text_input("Created by")
        category = st.selectbox("Category", options=["school", "work", "personal"])

        submitted = st.form_submit_button("Submit")
        
        if submitted:
            try:
                todo_data = {
                    "name": name,
                    "description": description,
                    "created_at": created_at,
                    "created_by": created_by,
                    "category": category,
                    "is_done": False 
                }
                new_todo = Todo(**todo_data)
                add_todo(new_todo)
                st.success("Todo added successfully!")
            except ValidationError as e:
                st.error(f"Validation error: {e}")

    st.write("### All Todos")
    display_todos()
    
if __name__ == "__main__":
    main()
