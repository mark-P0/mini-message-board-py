from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from app.exceptions import NotFoundException
from app.routes.messages.router import MessagesRouter
from app.routes.router import IndexRouter
from app.templates import (
    NotFoundTemplate,
)

app = FastAPI()

app.include_router(IndexRouter)
app.include_router(MessagesRouter)


@app.exception_handler(NotFoundException)
def not_found(*_):
    return HTMLResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=NotFoundTemplate.render(),
    )
