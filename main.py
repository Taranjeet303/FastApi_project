from fastapi import FastAPI
app= FastAPI()
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