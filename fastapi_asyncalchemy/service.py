from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_asyncalchemy.models import *


async def getContactById(session: AsyncSession) -> list[Contact]:
    result = await session.execute(select(Contact).order_by(City.id()))
    return result.scalars().all()
# функції не дороблені, але не можемо їх тестувати, бо не працює код

def addContact(session: AsyncSession, id: int, name: str, description: str):
    newContact = Contact(id = id, name = name, description = description)
    session.add(newContact)
    return newContact
    