import typing as T

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from messages import add_message, messages
from templates.templates import IndexTemplate, NewMessageTemplate

app = FastAPI()


class NewMessageRoute:
    class RequestBodyRaw(BaseModel):
        user: str
        text: str

    class ResponseBody(BaseModel):
        message: str

    RequestBody = T.Annotated[RequestBodyRaw, Form()]

    @staticmethod
    @app.post("/new")
    def new_message(body: RequestBody) -> ResponseBody:
        add_message(user=body.user, text=body.text)

        return NewMessageRoute.ResponseBody(
            message="Message added successfully",
        )


@app.get("/", response_class=HTMLResponse)
def show_messages():
    """
    https://fastapi.tiangolo.com/advanced/custom-response/#html-response

    FastAPI also has a built-in templating syntax, but this seems simpler
    https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates
    """

    return IndexTemplate.render(
        title="Mini Messageboard",
        messages=messages,
    )


@app.get("/new", response_class=HTMLResponse)
def show_new_message_form():
    return NewMessageTemplate.render(
        title="Mini Messageboard",
    )
