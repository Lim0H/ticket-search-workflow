from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

__all__ = ["init_fastapi"]


def init_fastapi(routers: list[APIRoute], version="v1") -> FastAPI:
    app = FastAPI(root_path=f"/api/{version}")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    for router in routers:
        app.include_router(router)

    return app
