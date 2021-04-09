from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#@app.get("/getuser/{username}/")
#async def helloo(username: str):
#    return {"Hello " + username}
  

class Contact(BaseModel):
    id:int
    name:str
    desceiption:str
@app.get('/contact')
async def create_contact(contact: Contact):
    id = contact.id
    name = contact.name
    desceiption = contact.desceiption

