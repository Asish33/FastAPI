from model import Todo

from fastapi import FastAPI,HTTPException

todos : list[Todo]=[]

app = FastAPI()

@app.get('/todo', response_model=list[Todo])
def get_all_todos():
    return todos