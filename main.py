import asyncio
import typer
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from fastapi_asyncalchemy.exceptions import DuplicatedEntryError
from fastapi_asyncalchemy.db.base import init_models
from fastapi_asyncalchemy.db.base import get_session
from fastapi_asyncalchemy import service

app = FastAPI()
cli = typer.Typer()

class Contact(BaseModel):
    id:int
    name:str
    description:str

@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")

@app.get("/contacts/{id}", response_model=list[Contact])
async def getContactById(session: AsyncSession = Depends(get_session)):
    contact = await service.getContactById(session)
    return [Contact(name=contact.name, description=contact.description)]

@app.post("/contacts")
async def addContact(contact: Contact, session: AsyncSession = Depends(get_session)):
    contact = service.addContact(session, contact.id, contact.name, contact.description)
    try:
        await session.commit()
        return contact
    except IntegrityError as ex:
        await session.rollback()
        raise DuplicatedEntryError("The contact is already stored")

if __name__ == "__main__":
    cli()
