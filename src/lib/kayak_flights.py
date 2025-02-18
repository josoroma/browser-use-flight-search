"""
kayak_flights.py

This module provides functionality to build a Kayak Flights URL for searching flights.
"""

from urllib.parse import urlencode

def kayak_flights_build_url(departure: str, destination: str, date: str, return_date: str = None) -> str:
    """
    Build a URL for searching flights on Kayak.

    Args:
        departure (str): The departure airport code.
        destination (str): The destination airport code.
        date (str): The departure date in YYYY-MM-DD format.
        return_date (str, optional): The return date in YYYY-MM-DD format. Defaults to None.

    Returns:
        str: The constructed URL for the flight search.
    """
    base_url = "https://www.kayak.com/flights"
    query_params = {
        "sort": "bestflight_a"
    }

    if return_date:
        url = f"{base_url}/{departure}-{destination}/{date}/{return_date}"
    else:
        url = f"{base_url}/{departure}-{destination}/{date}"

    return f"{url}?{urlencode(query_params)}"
