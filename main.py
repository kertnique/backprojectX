from fastapi import FastAPI

app = FastAPI()


@app.get("/getuser/{username}/")
async def helloo(username: str):
    return {"Hello " + username}
  
