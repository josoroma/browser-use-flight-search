"""
typings.py

This module defines Pydantic models for representing flight details and airline information
from different sources such as Google and Kayak. These models are used to structure and validate
the data retrieved from these sources.
"""

from typing import List

from pydantic import BaseModel


class GoogleFlightDetails(BaseModel):
    """
    Represents the details of a flight from Google.
    """

    departure: str
    arrival: str
    duration: str
    route: str
    price: str
    emissions: str
    emissions_percent: str


class GoogleAirline(BaseModel):
    """
    Represents an airline with a list of flights.

    Attributes:
        name (str): The name of the airline.
        flights (List[GoogleFlightDetails]): A list of flights operated by the airline.
    """

    name: str
    flights: List[GoogleFlightDetails]


class GoogleControllerOutput(BaseModel):
    """
    Represents the output from the Google controller.

    Attributes:
        airlines (List[GoogleAirline]): A list of airlines with their respective flights.
    """

    airlines: List[GoogleAirline] = []


class KayakFlightDetails(BaseModel):
    """
    Represents the details of a flight from Kayak.
    """

    departure: str
    arrival: str
    duration: str
    route: str
    price: str
    cabin: str


class KayakAirline(BaseModel):
    """
    Represents an airline with a list of flights from Kayak.

    Attributes:
        name (str): The name of the airline.
        flights (List[KayakFlightDetails]): A list of flights operated by the airline.
    """

    name: str
    flights: List[KayakFlightDetails]


class KayakControllerOutput(BaseModel):
    """
    Represents the output from the Kayak controller.

    Attributes:
        airlines (List[KayakAirline]): A list of airlines with their respective flights.
    """

    airlines: List[KayakAirline] = []
