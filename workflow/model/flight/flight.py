from datetime import datetime

from sqlmodel import Field, Relationship

from workflow.core import BaseModel, IdType, SeatClass
from workflow.core import FlightStatus
from workflow.model.flight.airline import AirLine, AirPort


class Flight(BaseModel, table=True):
    __tablename__ = "flights"

    flight_id: IdType = Field(default=None, primary_key=True)
    airline_id: int = Field(foreign_key="airlines.airline_id")
    departure_airport_id: int = Field(foreign_key="airports.airport_id")
    arrival_airport_id: int = Field(foreign_key="airports.airport_id")

    departure_time: datetime
    arrival_time: datetime
    flight_duration_in_seconds: int
    flight_status: FlightStatus = Field(default=FlightStatus.FLIGHT_WAITING)

    airline: AirLine = Relationship()
    departure_airport: AirPort = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "AirPort.airport_id==Flight.departure_airport_id"
        }
    )
    arrival_airport: AirPort = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "AirPort.airport_id==Flight.arrival_airport_id"
        }
    )


class Seat(BaseModel, table=True):
    __tablename__ = "seats"

    seat_id: IdType = Field(default=True, primary_key=True)
    flight_id: int = Field(foreign_key="flights.flight_id")

    seat_number: str = Field(max_length=255)
    seat_class: SeatClass = Field(default=SeatClass.ECONOMY_CLASS)
    is_available: bool = Field(default=True)

    flight: Flight = Relationship()


__all__ = ["Flight", "Seat"]
