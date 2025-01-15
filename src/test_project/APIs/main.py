from fastapi import FastAPI, Form
from enum import Enum
from http import HTTPStatus

app = FastAPI()

@app.get("/")
def root():
    """ Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

class ItemEnum(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/restric_items/{item_id}")
def read_item(item_id: ItemEnum):
    return {"item_id": item_id}

@app.get("/query_items")
def read_item(item_id: int):
    return {"item_id": item_id}


database = {'username': [ ], 'password': [ ]}

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    username_db = database['username']
    password_db = database['password']
    if username not in username_db and password not in password_db:
        with open('database.csv', "a") as file:
            file.write(f"{username}, {password}\n")
        username_db.append(username)
        password_db.append(password)
    return "login saved"










# from contextlib import asynccontextmanager
# from fastapi import FastAPI

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     print("Hello")
#     yield
#     print("Goodbye")

# app = FastAPI(lifespan=lifespan)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}