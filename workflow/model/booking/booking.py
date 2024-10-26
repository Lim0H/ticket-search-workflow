from datetime import datetime, date
from decimal import Decimal

from pydantic import EmailStr
from pydantic_extra_types.currency_code import Currency
from pydantic_extra_types.phone_numbers import PhoneNumber
from sqlmodel import Field, Relationship

from workflow.core import BaseModel, PaymentMethod, IdType, BookingStatus
from workflow.core import PaymentStatus
from workflow.model import Seat, Flight


class Passenger(BaseModel, table=True):
    __tablename__ = "passengers"

    passenger_id: IdType = Field(primary_key=True, default=None)
    first_name: str
    last_name: str
    date_of_birth: date
    passport_number: str = Field(max_length=255)
    contact_phone: PhoneNumber
    contact_email: EmailStr


class Booking(BaseModel, table=True):
    __tablename__ = "bookings"

    booking_id: IdType = Field(primary_key=True, default=None)
    booking_datetime: datetime = Field(default_factory=datetime.utcnow())  # type: ignore
    booking_status: BookingStatus = Field(default=BookingStatus.BOOKED)

    passenger: Passenger = Relationship()
    seat: Seat = Relationship()
    flight: Flight = Relationship()


class BookingPayment(BaseModel, table=True):
    __tablename__ = "booking_payments"

    payment_id: IdType = Field(primary_key=True, default=None)
    amount: Decimal
    currency: Currency
    payment_datetime: datetime
    payment_status: PaymentStatus
    payment_method: PaymentMethod

    booking: Booking = Relationship()


__all__ = ["Booking", "BookingPayment", "Passenger"]
