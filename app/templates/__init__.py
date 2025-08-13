"""
https://jinja.palletsprojects.com/en/stable/api/#basics
"""

import typing as T

from jinja2 import Environment, PackageLoader, select_autoescape

from app.db.messages import Message

env_loader = PackageLoader(package_name="app.templates", package_path="html")
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


class MessageDetailsTemplate:
    name = "message-details.html"

    class Context(T.TypedDict):
        message: Message

    @classmethod
    def render(cls, **kwargs: T.Unpack[Context]):
        return render_template(cls.name, **kwargs)
