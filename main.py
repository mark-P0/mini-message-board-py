import typing as T

from fastapi import FastAPI, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

from db.messages import add_message, messages
from templates.templates import (
    IndexTemplate,
    NewMessageTemplate,
    NotFoundTemplate,
)

app = FastAPI()


class NewMessageRoute:
    class RequestBodyRaw(BaseModel):
        user: str
        text: str

    RequestBody = T.Annotated[RequestBodyRaw, Form()]

    @staticmethod
    @app.post(
        "/new",
        response_class=RedirectResponse,
        status_code=status.HTTP_303_SEE_OTHER,
    )
    def new_message(body: RequestBody):
        add_message(user=body.user, text=body.text)

        return "/"


class NotFoundException(Exception): ...


@app.exception_handler(NotFoundException)
def not_found(*_):
    return HTMLResponse(content=NotFoundTemplate.render())


@app.get("/", response_class=HTMLResponse)
def show_messages():
    """
    https://fastapi.tiangolo.com/advanced/custom-response/#html-response

    FastAPI also has a built-in templating syntax, but this seems simpler
    https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates
    """

    return IndexTemplate.render(
        messages=messages,
    )


@app.get("/new", response_class=HTMLResponse)
def show_new_message_form():
    return NewMessageTemplate.render()
