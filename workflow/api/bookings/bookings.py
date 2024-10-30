from fastapi import APIRouter
from fastapi_restful.cbv import cbv

__all__ = ["bookings_router"]

bookings_router = APIRouter(prefix="/bookings")


@cbv(bookings_router)
class BookingsResource:
    pass
