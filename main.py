from fastapi import FastAPI
from pydantic import BaseModel
from deta import Deta


app = FastAPI()
deta = Deta()
db = deta.Base("people")


class Person(BaseModel):
    name: str
    age: int


@app.get("/")
def hello():
    return "Hello from Deta!"


@app.post("/people")
def save_person(person: Person):
    resp = db.put(person.dict())
    return resp


@app.get("/people")
def people_list():
    return db.fetch()
