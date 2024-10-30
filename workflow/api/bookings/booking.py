from fastapi import APIRouter
from fastapi_restful.cbv import cbv

__all__ = ["booking_router"]

booking_router = APIRouter(prefix="/booking/{booking_id}")


@cbv(booking_router)
class BookingResource:
    pass
