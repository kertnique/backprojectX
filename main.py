from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


db = {}


class Contact(BaseModel):
    id:int
    name:str
    description:str


@app.get('/contacts/{id}', response_model=Contact)
async def create_contact(id: int):
    contact = db[id]
    return contact


@app.post('/contacts')
async def post(contact: Contact):
    db[contact.id] = contact
    return contact
