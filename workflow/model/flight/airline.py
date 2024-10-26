from pydantic_extra_types.country import CountryShortName, CountryAlpha3
from pydantic_extra_types.timezone_name import TimeZoneName
from sqlmodel import Field, Relationship

from workflow.core import BaseModel, IdType


class Country(BaseModel, table=True):
    __tablename__ = "countries"

    country_id: IdType = Field(default=None, primary_key=True)
    country_name: CountryShortName
    country_code: CountryAlpha3


class AirPort(BaseModel, table=True):
    __tablename__ = "airports"

    airport_id: IdType = Field(default=None, primary_key=True)
    airport_name: str
    city: str
    iata_code: str = Field(unique=True)
    timezone: TimeZoneName

    country: Country = Relationship()


class AirLine(BaseModel, table=True):
    __tablename__ = "airlines"

    airline_id: IdType = Field(default=True, primary_key=True)
    airline_name: str
    iata_code: str = Field(unique=True)
    country: Country = Relationship()


__all__ = ["AirLine", "Country", "AirPort"]
