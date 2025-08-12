from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from messages import messages
from templates.templates import render_template

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    """
    https://fastapi.tiangolo.com/advanced/custom-response/#html-response

    FastAPI also has a built-in templating syntax, but this seems simpler
    https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates
    """

    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    ...
