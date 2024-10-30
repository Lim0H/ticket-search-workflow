from random import choice

import factory
from async_factory_boy.factory.sqlalchemy import AsyncSQLAlchemyFactory

from tests.model_factory.conftest import get_faker
from tests.model_factory.fligth.airline import AirLineFactory, AirPortFactory
from workflow import Flight, Seat, FlightStatus, sc_postgres_session

__all__ = ["FlightFactory", "SeatFactory"]


class FlightFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Flight
        sqlalchemy_session = sc_postgres_session

    flight_id = factory.Sequence(lambda n: n + 1)

    departure_time = factory.Sequence(
        lambda x: get_faker().date_time_this_month()
    )
    arrival_time = factory.Sequence(
        lambda x: get_faker().date_time_this_month()
    )
    flight_duration_in_seconds = factory.Sequence(
        lambda x: get_faker().random_int(2000, 10000)
    )
    flight_status = factory.Sequence(
        lambda x: choice(list(FlightStatus.__iter__()))
    )

    airline = factory.SubFactory(AirLineFactory)
    departure_airport = factory.SubFactory(AirPortFactory)
    arrival_airport = factory.SubFactory(AirPortFactory)


class SeatFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Seat
        sqlalchemy_session = sc_postgres_session

    seat_id = factory.Sequence(lambda n: n + 1)

    seat_number = factory.Sequence(lambda n: get_faker().seat_number())
    seat_class = factory.Sequence(lambda x: get_faker().seat_class())
    is_available = factory.Sequence(lambda x: get_faker().is_seat_available())

    flight = factory.SubFactory(FlightFactory)
