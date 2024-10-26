from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from workflow.core import BaseModel, IdType, SeatClass
from workflow.core import FlightStatus

if TYPE_CHECKING:
    from workflow.model import AirLine, AirPort


class Flight(BaseModel, table=True):
    __tablename__ = "flights"

    flight_id: IdType = Field(default=None, primary_key=True)
    departure_time: datetime
    arrival_time: datetime
    flight_duration_in_seconds: int
    flight_status: FlightStatus = Field(default=FlightStatus.FLIGHT_WAITING)

    airline: "AirLine" = Relationship()
    departure_airport: "AirPort" = Relationship()
    arrival_airport: "AirPort" = Relationship()


class Seat(BaseModel, table=True):
    __tablename__ = "seats"

    seat_id: IdType = Field(default=True, primary_key=True)
    seat_number: str = Field(max_length=255)
    seat_class: SeatClass = Field(default=SeatClass.ECONOMY_CLASS)
    is_available: bool = Field(default=True)

    flight: Flight = Relationship()


__all__ = ["Flight", "Seat"]
