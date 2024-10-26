from enum import Enum, auto

__all__ = ["PaymentStatus", "PaymentMethod", "BookingStatus"]


class PaymentStatus(Enum):
    STARTED = auto()
    IN_PROCESSING = auto()
    COMPLETED = auto()
    ERROR = auto()


class PaymentMethod(Enum):
    PAYPAL = auto()
    CREDIT_CARD = auto()


class BookingStatus(Enum):
    BOOKED = auto()
    CANCELED_BY_USER = auto()
    CANCELED_BY_AIRLINE = auto()
