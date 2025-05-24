# FastAPI Todo App

Exploring FastAPI by building this Todo API project

---

## Features

- Get all todos  
- Add a new todo  
- Get a todo by ID  
- Update a todo by ID  
- Delete a todo by ID  

---

## How to Run

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Run the app:

```bash
uvicorn main:app --reload
```

3. Open your browser and visit:  
`http://127.0.0.1:8000/docs`  
to explore and test the API using the interactive Swagger UI.

---

## Testing with Postman

You can test the API endpoints using Postman:

- GET `/todos` — Get all todos  
- POST `/addTodo` — Add new todo (send JSON body)  
- GET `/todos/{todo_id}` — Get todo by ID  
- PUT `/todos/{todo_id}` — Update todo by ID (send JSON body)  
- DELETE `/todo/{todo_id}` — Delete todo by ID  

## Example Todo JSON

```json
{
  "id": 1,
  "title": "Buy milk",
  "description": "Remember to buy milk from the store",
  "status":false
}
```
