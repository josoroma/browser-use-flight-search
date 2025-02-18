"""
google_flights.py

This module provides functionality to build a Google Flights URL for searching flights.
"""

def google_flights_build_url(departure: str, destination: str, date: str, return_date: str = None) -> str:
    """
    Build a Google Flights URL for searching flights on Google.

    Args:
        departure (str): The departure airport code.
        destination (str): The destination airport code.
        date (str): The departure date in YYYY-MM-DD format.
        return_date (str, optional): The return date in YYYY-MM-DD format. Defaults to None.

    Returns:
        str: The constructed Google Flights URL.
    """
    base_url = "https://www.google.com/travel/flights"
    query = f"?q=flights from {departure} to {destination} on {date}"
    if return_date:
        query += f" returning on {return_date}"
    return f"{base_url}{query}&curr=USD"
