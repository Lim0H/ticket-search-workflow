from random import randint

import factory
from async_factory_boy.factory.sqlalchemy import AsyncSQLAlchemyFactory

from tests.model_factory.conftest import get_faker
from tests.model_factory.fligth.fligth import SeatFactory, FlightFactory
from workflow import (
    Passenger,
    Booking,
    BookingPayment,
    BookingStatus,
    PaymentStatus,
    PaymentMethod,
    sc_postgres_session,
)

__all__ = ["PassengerFactory", "BookingFactory", "BookingPaymentFactory"]


class PassengerFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Passenger
        sqlalchemy_session = sc_postgres_session

    passenger_id = factory.Sequence(lambda n: n + 1)
    first_name = factory.Sequence(lambda x: get_faker().first_name())
    last_name = factory.Sequence(lambda x: get_faker().last_name())
    date_of_birth = factory.Sequence(lambda x: get_faker().date_of_birth())
    passport_number = factory.Sequence(lambda x: get_faker().passport_number())
    contact_phone = factory.Sequence(lambda x: get_faker().phone_number())
    contact_email = factory.Sequence(lambda x: get_faker().email())


class BookingFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Booking
        sqlalchemy_session = sc_postgres_session

    booking_id = factory.Sequence(lambda n: n + 1)
    booking_datetime = factory.Sequence(
        lambda x: get_faker().date_time_this_month()
    )
    booking_status = BookingStatus.BOOKED

    seat = factory.SubFactory(SeatFactory)
    flight = factory.SubFactory(FlightFactory)


class BookingPaymentFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = BookingPayment
        sqlalchemy_session = sc_postgres_session

    payment_id = factory.Sequence(lambda n: n + 1)
    amount = factory.Sequence(lambda x: randint(1, 100))
    currency = factory.Sequence(lambda x: get_faker().currency_code())
    payment_datetime = factory.Sequence(
        lambda x: get_faker().date_time_this_month()
    )
    payment_status = PaymentStatus.COMPLETED
    payment_method = PaymentMethod.CREDIT_CARD

    booking = factory.SubFactory(BookingFactory)
