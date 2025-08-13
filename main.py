from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from messages import messages
from templates.templates import IndexTemplate, NewMessageTemplate

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
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
def new_message():
    return NewMessageTemplate.render(
        title="Mini Messageboard",
    )


if __name__ == "__main__":
    ...
