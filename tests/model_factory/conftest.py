from functools import lru_cache
from random import choice, randint

import pytest
from faker import Faker
from faker_airtravel import AirTravelProvider as AirTravelProviderBase

from workflow import SeatClass


class AirTravelProvider(AirTravelProviderBase):
    def seat_number(self):
        number = randint(1, 33)
        letter = choice(["A", "B", "C", "D"])
        return f"{number}{letter}"

    def seat_class(self):
        return choice(list(SeatClass.__iter__()))

    def is_seat_available(self):
        return choice([True, False])


@lru_cache
def get_faker():
    faker = Faker()
    faker.add_provider(AirTravelProvider)
    return faker


@pytest.fixture()
def faker():
    return get_faker()


__all__ = ["get_faker", "faker"]
