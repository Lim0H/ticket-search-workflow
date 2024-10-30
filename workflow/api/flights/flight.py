from fastapi import APIRouter
from fastapi_restful.cbv import cbv

__all__ = ["flight_router"]

flight_router = APIRouter(prefix="/flight/{flight_id}")


@cbv(flight_router)
class FlightResource:
    pass
