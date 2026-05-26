from fastapi import FastAPI
from pydantic import BaseModel,Field,validator
from typing import Optional
app= FastAPI()
class Login_request(BaseModel):
    username: str= Field(max_length=25,min_length=4)
    age:int=Field(gt=18,lt=80)
    sex: str
    nationality: Optional[str]=None

users ={
    1:{"name" : "Taranjeet Kaur","age" : 20},
    2:{"name" : "Anish","age" : 29},
    3:{"name" : "Tripti","age" : 17}
}
@app.get("/")
def home():
    return {"message":"Welcome User!"}
@app.get("/users/{user_id}")
def get_userid(user_id: int):
    return users.get(user_id, {"OOPS! Id not found!"})
@app.post("/users")
def create_user(user:dict):
    return {
        "message": "User created",
        "data" :user
    }


@app.post("/login")
def login(data:Login_request ):
    return {
        "message": f"user {data.username} has successfully logged in!"
    }
@app.put("/users")
def updated_userid(user_id:int, updated_user:dict):
    if user_id in users:
        users[user_id]= updated_user
        return{
            "message": "User updated",
            "data": users[user_id]
        }
    return {"error": "User not found"}
@app.delete("/users/{users.id}")
def del_userid(user_id: int):
    if user_id in users:
        deleted_user= users.pop(user_id)
        return{
            "message": "user id deleted sucessfully.",
            "data": deleted_user
        }
    return {"error": "User not found"}