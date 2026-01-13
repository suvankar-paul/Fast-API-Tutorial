from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome to FastAPI lectures": "This is the introduction endpoint."}


@app.get("/about")
def read_about():
    return {"About": "This API is built using FastAPI to demonstrate its features."}