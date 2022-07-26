from fastapi import FastAPI

app = FastAPI()


@app.get("book-cover")
def hello():
    return "Hello World"
