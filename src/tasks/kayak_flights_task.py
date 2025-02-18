"""
katak_flights_task.py

This module provides a function to create a formatted task description for searching flights on Kayak.
It uses a predefined JSON schema for the output format.
"""

import json

from src.constants import KAYAK_FLIGHT_SEARCH_JSON_SCHEMA


def get_kayak_flights_task(
    kayak_flights_url: str, departure: str, destination: str
) -> str:
    """
    Generate the task description for Kayak flights search.

    Args:
        kayak_flights_url (str): The URL to search on Kayak.
        departure (str): Departure airport code.
        destination (str): Destination airport code.

    Returns:
        str: Formatted task description.
    """

    task_description = (
        f"- Visit Kayak Flights at {kayak_flights_url} and wait for the flight search results to fully load.\n"
        "- Extract all the flights scrollable on the page.\n"
        f"- With the extracted data, please provide the best JSON output grouped by airline "
        f"(extend JSON output with `route` attribute and value `{departure}-{destination}`):\n\n"
        f"{json.dumps(KAYAK_FLIGHT_SEARCH_JSON_SCHEMA, indent=4)}\n"
    )

    return task_description
