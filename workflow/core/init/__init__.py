from fastapi.routing import APIRoute

from .database import init_database
from .fastapi import init_fastapi


def init_application(routers: list[APIRoute], version="v1"):
    init_database()  # noqa: F405
    app = init_fastapi(routers=routers, version=version)  # noqa: F405
    return app
