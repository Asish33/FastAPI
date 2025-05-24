from model import Todo

from fastapi import FastAPI,HTTPException

todos : list[Todo]=[]

app = FastAPI()

@app.get('/todos', response_model=list[Todo])
def get_all_todos():
    return todos

@app.post('/addTodo', response_model=Todo)
def add_todo(todo:Todo):
    todos.append(todo)
    return todo

@app.get('/todos/{todo_id}', response_model=Todo)
def todo_by_id(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='No Todo Present with the given id')

@app.put('/todos/{todo_id}', response_model=Todo)
def update_todo_by_id(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo  
            return updated_todo
    raise HTTPException(status_code=404, detail='No Todo present with given Id')

@app.delete('/todo/{todo_id}', response_model=str)
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return 'todo with given id is deleted'
    raise HTTPException(status_code=404,detail='No Todo present with given id')
    