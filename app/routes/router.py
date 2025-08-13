from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from app.db.messages import Message
from app.routes.paths import RoutePath
from app.templates import (
    IndexTemplate,
)

IndexRouter = APIRouter()


@IndexRouter.get(RoutePath.INDEX, response_class=HTMLResponse)
def show_messages():
    """
    https://fastapi.tiangolo.com/advanced/custom-response/#html-response

    FastAPI also has a built-in templating syntax, but this seems simpler
    https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates
    """

    messages = Message.get_all()

    return IndexTemplate.render(messages=messages)
