from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

user_list = []

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}

@app.post("/register_user")
async def create_user(user: User):
    user_list.append(user)
    return {"message": "User created successfully"}

@app.get("/get_users")
async def get_users():
    return {"status": "success", "users": user_list}

@app.post("/login")
async def login(req_user: User):
    for user in user_list:
        if user.username == req_user.username and user.password == req_user.password:
            return {"status": "success"}
    return {"status": "failure"}

