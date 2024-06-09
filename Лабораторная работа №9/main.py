from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

todos = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do List API"}

@app.post("/todos/", response_model=TodoItem)
def create_todo_item(todo: TodoItem):
    todos.append(todo)
    return todo

@app.get("/todos/", response_model=List[TodoItem])
def get_todo_items():
    return todos

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, todo: TodoItem):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos[index] = todo
            return todo
    return None

@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(index)
            return {"message": "Todo item deleted"}
    return {"message": "Todo item not found"}
