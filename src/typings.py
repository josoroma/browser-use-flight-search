"""
Module: typings

This module defines Pydantic models for representing flight details and airline information
from different sources such as Google and Kayak. These models are used to structure and validate
the data retrieved from these sources.
"""
from typing import List
from pydantic import BaseModel


class GoogleFlightDetails(BaseModel):
    """
    Represents the details of a flight from Google.

    Attributes:
        departure (str): The departure time of the flight.
        arrival (str): The arrival time of the flight.
        duration (str): The duration of the flight.
        route (str): The route of the flight.
        price (str): The price of the flight.
        emissions (str): The emissions of the flight.
        emissions_percent (str): The emissions percentage of the flight.
    """
    departure: str
    arrival: str
    duration: str
    route: str
    price: str
    emissions: str
    emissions_percent: str


class Airline(BaseModel):
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
        airlines (List[Airline]): A list of airlines with their respective flights.
    """
    airlines: List[Airline] = []


class KayakFlightDetails(BaseModel):
    """
    Represents the details of a flight from Kayak.

    Attributes:
        departure (str): The departure time of the flight.
        arrival (str): The arrival time of the flight.
        duration (str): The duration of the flight.
        route (str): The route of the flight.
        price (str): The price of the flight.
        cabin (str): The cabin class of the flight.
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
