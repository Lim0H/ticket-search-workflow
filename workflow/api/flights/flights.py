from fastapi import APIRouter
from fastapi_restful.cbv import cbv

__all__ = ["flights_router"]

flights_router = APIRouter(prefix="/flights")


@cbv(flights_router)
class FlightsResource:
    pass
