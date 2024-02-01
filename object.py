from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import sqlite3

class Todo(BaseModel):
    name: str
    description: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    category: Optional[str] = None
    is_done: bool = False  # Default value set to False

    def __init__(self, **data):
        super().__init__(**data)
        if not self.created_at:
            self.created_at = datetime.now()

def init_db():
    conn = sqlite3.connect('todo.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS todos
                 (id INTEGER PRIMARY KEY, name TEXT, description TEXT, created_at DATETIME, created_by TEXT, category TEXT, is_done BOOLEAN)''')
    conn.commit()
    conn.close()

def add_todo(todo):
    conn = sqlite3.connect('todo.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO todos (name, description, created_at, created_by, category, is_done) VALUES (?, ?, ?, ?, ?, ?)", 
              (todo.name, todo.description, todo.created_at, todo.created_by, todo.category, todo.is_done))
    conn.commit()
    conn.close()

def get_todos():
    conn = sqlite3.connect('todo.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()
    conn.close()
    return todos

def update_task_completion(task_id, is_done):
    conn = sqlite3.connect('todo.sqlite')
    c = conn.cursor()
    c.execute("UPDATE todos SET is_done = ? WHERE id = ?", (is_done, task_id))
    conn.commit()
    conn.close()
