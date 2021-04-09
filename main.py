from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Contact(BaseModel):
    id:int
    name:str
    description:str
@app.get('/contacts')
async def create_contact(contact: Contact):
    id = contact.id
    name = contact.name
    description = contact.description
@app.post('/contacts')
async def post(contact: Contact):
    return Contact
