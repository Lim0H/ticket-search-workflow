from .bookings import booking_router, bookings_router
from .flights import flight_router, flights_router, airlines_router

ROUTERS = [
    flight_router,
    airlines_router,
    flights_router,
    booking_router,
    bookings_router,
]

__all__ = ["ROUTERS"]
