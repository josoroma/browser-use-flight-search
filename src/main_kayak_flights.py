"""
main_kayak_flights.py

This module performs a Kayak Flights search using an asynchronous agent.
"""

import asyncio

from browser_use import Agent, Controller
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.constants import OPENAPI_MODEL_NAME
from src.lib.kayak_flights import kayak_flights_build_url
from src.tasks.kayak_flights_task import get_kayak_flights_task
from src.typings import KayakControllerOutput

# Load environment variables from .env
load_dotenv(override=True)


async def kayak_flights_search_agent(
    departure: str, destination: str, date: str, return_date: str = None
) -> Agent | None:
    """
    Creates an agent to search for flights on Kayak.

    Parameters:
    departure (str): The departure location.
    destination (str): The destination location.
    date (str): The departure date.
    return_date (str, optional): The return date. Defaults to None.

    Returns:
    Agent | None: The agent configured to search for flights or None if an error occurs.
    """

    kayak_flights_url = kayak_flights_build_url(
        departure, destination, date, return_date
    )
    kayak_flights_task_description = get_kayak_flights_task(
        kayak_flights_url, departure, destination
    )
    controller = Controller(output_model=KayakControllerOutput)

    try:
        kayak_flights_agent = Agent(
            task=kayak_flights_task_description,
            llm=ChatOpenAI(model=OPENAPI_MODEL_NAME),
            controller=controller,
        )
        return kayak_flights_agent
    except asyncio.TimeoutError:
        print("ERROR: Flight search took too long and timed out.")
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None
    finally:
        await asyncio.sleep(5)
