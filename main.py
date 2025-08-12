from fastapi import FastAPI

from messages import Message, messages
from utils.todo import TODO

app = FastAPI()


@app.get("/")
def index() -> list[Message]:
    TODO("respond with html")
    return messages


if __name__ == "__main__":
    ...
