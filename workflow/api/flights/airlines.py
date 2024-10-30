from fastapi import APIRouter
from fastapi_restful.cbv import cbv

__all__ = ["airlines_router"]

airlines_router = APIRouter(prefix="/airlines")


@cbv(airlines_router)
class AirLinesResource:
    pass
