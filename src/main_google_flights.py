"""
main_google_flights.py

This module performs a Google Flights search using an asynchronous agent.
"""

import asyncio
from dotenv import load_dotenv

from browser_use import Agent, Controller
from langchain_openai import ChatOpenAI

from src.constants import OPENAPI_MODEL_NAME
from src.lib.google_flights import google_flights_build_url
from src.tasks.google_flights_task import get_google_flights_task
from src.typings import GoogleControllerOutput

# Load environment variables from .env
load_dotenv(override=True)

async def google_flights_search_agent(
    departure: str, destination: str, date: str, return_date: str = None
) -> Agent | None:
    """
    Perform a Google Flights search using an asynchronous agent.

    Parameters:
    departure (str): The departure location.
    destination (str): The destination location.
    date (str): The departure date.
    return_date (str, optional): The return date. Defaults to None.

    Returns:
    Agent | None: The Google Flights search agent or None if an error occurs.
    """
    google_flights_url = google_flights_build_url(departure, destination, date, return_date)
    google_flights_task_description = get_google_flights_task(google_flights_url, departure, destination)

    controller = Controller(output_model=GoogleControllerOutput)

    try:
        google_flights_agent = Agent(
            task=google_flights_task_description,
            llm=ChatOpenAI(model=OPENAPI_MODEL_NAME),
            controller=controller,
        )
        return google_flights_agent
    except asyncio.TimeoutError:
        print("ERROR: Flight search took too long and timed out.")
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None
    finally:
        await asyncio.sleep(5)
