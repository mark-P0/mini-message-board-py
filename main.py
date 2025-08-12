from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return dict(hello="world")


if __name__ == "__main__":
    ...
