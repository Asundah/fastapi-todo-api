from fastapi import FastAPI
from pydantic import BaseModel

# FASTAPI app
app = FastAPI(
    title = "Todo API", 
    description = "Complete CRUD API for managing todos!"
)

class TodoCreate(BaseModel):
    title:str
    completed:bool = False

class TodoResponse(BaseModel):
    id:int
    title:str
    completed:bool

# In Memory Database
# Stores todos in memory
todos = []
next_id = 1

# CREATE - Add a new todo
@app.post("/todos", response_model = TodoResponse)
def create_todo(todo:TodoCreate):
    global next_id
    new_todo = {
        "id": next_id,
        "title": todo.title,
        "completed": todo.completed
    }
    todos.append(new_todo)
    next_id = next_id + 1
    return new_todo

# READ ALL - Get all todos
@app.get("/todos", response_model = list[TodoResponse])
def get_todos():
    return todos

# READ ONE - Get a specific todo
@app.get("/todo/{todo_id}", response_model = TodoResponse)
def get_todo(todo_id:int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return {"error":"Todo not found"},404

# UPDATE - Update a todo
@app.put("/todos/{todo_id}", response_model = TodoResponse)
def update_todo(todo_id, updated_todo:TodoCreate):
    for todo in todos:
        if todo["id"] == todo_id:
            # update only the fields provided
            todo["title"] = updated_todo.title
            todo["completed"] = update_todo.completed
            return todo
    return {"error":"Todo not found"},404

# DELETE - Delet a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return{"message":"Todo deleted successfully"}
    return {"error":"Todo not found"},404