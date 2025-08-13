"""
https://jinja.palletsprojects.com/en/stable/api/#basics
"""

import typing as T

from jinja2 import Environment, FileSystemLoader, select_autoescape

from db.messages import Message

env_loader = FileSystemLoader("./templates/html")
env = Environment(loader=env_loader, autoescape=select_autoescape())


def render_template(template_name: str, **kwargs: T.Any):
    template = env.get_template(template_name)
    rendered = template.render(**kwargs)

    return rendered


class NotFoundTemplate:
    name = "not-found.html"

    class Context(T.TypedDict): ...

    @classmethod
    def render(cls, **kwargs: T.Unpack[Context]):
        return render_template(cls.name, **kwargs)


class IndexTemplate:
    name = "index.html"

    class Context(T.TypedDict):
        messages: list[Message]

    @classmethod
    def render(cls, **kwargs: T.Unpack[Context]):
        return render_template(cls.name, **kwargs)


class NewMessageTemplate:
    name = "new-message.html"

    class Context(T.TypedDict): ...

    @classmethod
    def render(cls, **kwargs: T.Unpack[Context]):
        return render_template(cls.name, **kwargs)
