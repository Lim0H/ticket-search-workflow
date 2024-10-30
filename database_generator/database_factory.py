import asyncio
import logging

from tests.model_factory import (
    BookingFactory,
    BookingPaymentFactory,
    FlightFactory,
    SeatFactory,
)
from workflow import (
    async_init_database,
)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def async_range(*args):
    for i in range(*args):
        yield i
        await asyncio.sleep(0)


async def _gen_database():
    await async_init_database()
    for _ in range(10000):
        # gen FlightFactory
        flight = await FlightFactory.create()
        log.info(f"Flight: {flight}")
        for seat_number_int in range(1, 34):
            for seat_number_letter in ("A", "B", "C", "D"):
                seat = await SeatFactory.create(
                    flight=flight,
                    seat_number=f"{seat_number_int}{seat_number_letter}",
                )
                if not seat.is_available:
                    booking = await BookingFactory.create(
                        flight=flight,
                        seat=seat,
                    )
                    await BookingPaymentFactory.create(
                        booking=booking,
                    )


def gen_database():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(_gen_database())
