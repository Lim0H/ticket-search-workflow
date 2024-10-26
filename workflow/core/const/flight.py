from enum import Enum, auto

__all__ = ["FlightStatus", "SeatClass"]


class FlightStatus(Enum):
    FLIGHT_WAITING = auto()
    FLIGHT_STARTED = auto()
    FLIGHT_ENDED = auto()
    CANCELED = auto()


class SeatClass(Enum):
    FIRST_CLASS = auto()
    BUSINESS_CLASS = auto()
    ECONOMY_CLASS = auto()
