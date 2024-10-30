import factory
from async_factory_boy.factory.sqlalchemy import AsyncSQLAlchemyFactory

from tests.model_factory.conftest import get_faker
from workflow import AirPort, AirLine, Country, sc_postgres_session

__all__ = ["CountryFactory", "AirPortFactory", "AirLineFactory"]


class CountryFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = Country
        sqlalchemy_session = sc_postgres_session
        sqlalchemy_get_or_create = ("country_code",)

    country_id = factory.Sequence(lambda n: n + 1)
    country_name = factory.Sequence(lambda x: get_faker().country())
    country_code = factory.Sequence(lambda x: get_faker().country_code())


class AirPortFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = AirPort
        sqlalchemy_session = sc_postgres_session
        sqlalchemy_get_or_create = ("iata_code",)

    airport_id = factory.Sequence(lambda n: n + 1)
    airport_name = factory.Sequence(lambda x: get_faker().airport_name())
    city = factory.Sequence(lambda x: get_faker().city())
    iata_code = factory.Sequence(lambda x: get_faker().airport_iata())
    timezone = factory.Sequence(lambda x: get_faker().timezone())

    country = factory.SubFactory(CountryFactory)


class AirLineFactory(AsyncSQLAlchemyFactory):
    class Meta:
        model = AirLine
        sqlalchemy_session = sc_postgres_session
        sqlalchemy_get_or_create = ("iata_code",)

    airline_id = factory.Sequence(lambda n: n + 1)
    airline_name = factory.Sequence(lambda x: get_faker().airline())
    iata_code = factory.Sequence(lambda x: get_faker().airport_iata())
    country = factory.SubFactory(CountryFactory)
