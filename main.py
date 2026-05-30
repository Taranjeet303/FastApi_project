from fastapi import FastAPI
from pydantic import BaseModel,Field,validator
from typing import Optional,List
from fastapi import FastAPI, HTTPException, Depends

from sqlalchemy.orm import Session



from database import get_db
from models import User
from schemas import UserCreate, UserResponse


app=FastAPI(title="integration with sql")




class Login_request(BaseModel):
    username: str= Field(max_length=25,min_length=4)
    age:int=Field(gt=18,lt=80)
    sex: str
    nationality: Optional[str]=None

# users ={
#    101:{"name" : "Taranjeet Kaur","age" : 20},
#     102:{"name" : "Anish","age" : 29},
#     103:{"name" : "Tripti","age" : 17},
#     104: {"name" : "kailash", "age": 56}
# }
# @app.get("/")
# def home():
#     return {"message":"Welcome User!"}
# @app.get("/users/{user_id}")
# def get_userid(user_id: int):
#     return users.get(user_id, {"OOPS! Id not found!"})
# @app.post("/users")
# def create_user(user:dict):
#     return {
#         "message": "User created",
#         "data" :user
#     }


# @app.post("/login")
# def login(data:Login_request ):
#     return {
#         "message": f"user {data.username} has successfully logged in!"
#     }
# @app.put("/users")
# def updated_userid(user_id:int, updated_user:dict):
#     if user_id in users:
#         users[user_id]= updated_user
#         return{
#             "message": "User updated",
#             "data": users[user_id]
#         }
#     return {"error": "User not found"}
# @app.delete("/users/{users.id}")
# def del_userid(user_id: int):
#     if user_id in users:
#         deleted_user= users.pop(user_id)
#         return{
#             "message": "user id deleted sucessfully.",
#             "data": deleted_user
#         }
#     return {"error": "User not found"}
@app.post("/")
def home():
    return {
        "message": "hello user!"
    }

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    return user

@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    updated_user: UserCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    user.name = updated_user.name
    user.age = updated_user.age

    db.commit()
    db.refresh(user)

    return user

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}