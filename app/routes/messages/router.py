import typing as T

from fastapi import APIRouter, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

from app.db.messages import Message
from app.exceptions import NotFoundException
from app.routes.paths import RoutePath
from app.templates import (
    MessageDetailsTemplate,
    NewMessageTemplate,
)

MessagesRouter = APIRouter()


class NewMessageRoute:
    class RequestBodyRaw(BaseModel):
        user: str
        text: str

    RequestBody = T.Annotated[RequestBodyRaw, Form()]

    @staticmethod
    @MessagesRouter.post(
        RoutePath.Messages.NEW,
        response_class=RedirectResponse,
        status_code=status.HTTP_303_SEE_OTHER,
    )
    def new_message(body: RequestBody):
        Message.add_one(user=body.user, text=body.text)

        return RoutePath.INDEX


@MessagesRouter.get(RoutePath.Messages.NEW, response_class=HTMLResponse)
def show_new_message_form():
    return NewMessageTemplate.render()


@MessagesRouter.get(RoutePath.Messages.ID, response_class=HTMLResponse)
def show_message(message_id: str):
    message = Message.get_one(message_id)
    if message is None:
        raise NotFoundException()

    return MessageDetailsTemplate.render(message=message)
