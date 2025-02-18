"""
google_flights_task.py

This module provides a function to create a formatted task description for searching flights on Google.
It uses a predefined JSON schema for the output format.
"""

import json

from src.constants import GOOGLE_FLIGHT_SEARCH_JSON_SCHEMA


def get_google_flights_task(
    google_flights_url: str, departure: str, destination: str
) -> str:
    """
    Generates a task description for searching flights on Google Flights.

    Args:
        google_flights_url (str): The URL to search on Google Flights.
        departure (str): The departure location.
        destination (str): The destination location.

    Returns:
        str: Formatted task description.
    """

    task_description = (
        f"- Visit Google Flights at {google_flights_url} and wait for the flight search results to fully load.\n"
        "- Extract all the flights scrollable on the page.\n"
        f"- With the extracted data, please provide the best JSON output grouped by airline "
        f"(extend JSON output with `route` attribute and value `{departure}-{destination}`):\n\n"
        f"{json.dumps(GOOGLE_FLIGHT_SEARCH_JSON_SCHEMA, indent=4)}\n"
    )

    return task_description
