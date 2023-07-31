from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():

  text = {"message": "hi chance"}
  return text