"""
main.py

This module executes flight search agents for Google Flights and Kayak.
It expects command line arguments for departure, destination, date, and optional return date.
The results from both agents are printed in a structured format.
"""

import asyncio
import sys
from dotenv import load_dotenv
from src.lib.utils import print_structured_result
from src.main_kayak_flights import kayak_flights_search_agent
from src.main_google_flights import google_flights_search_agent
from src.lib.run import run_agent

# Load environment variables from .env
load_dotenv(override=True)

async def main():
    """
    Main function to execute flight search agents for Google Flights and Kayak.
    
    Expects command line arguments for departure, destination, date, and optional return date.
    
    Parameters:
    None
    
    Returns:
    None
    """
    if len(sys.argv) < 4:
        print("Usage: poetry run python main.py SFO JFK 2025-10-10 2025-11-10")
        sys.exit(1)

    departure = sys.argv[1]
    destination = sys.argv[2]
    date = sys.argv[3]
    return_date = sys.argv[4] if len(sys.argv) > 4 else None

    # Run Google Flights Agent
    google_flights_agent = await google_flights_search_agent(
        departure, destination, date, return_date
    )
    google_flights_run_result = await run_agent(google_flights_agent)

    # Run Kayak Flights Agent
    kayak_flights_agent = await kayak_flights_search_agent(
        departure, destination, date, return_date
    )
    kayak_flights_run_result = await run_agent(kayak_flights_agent)
    
    # Print Google and Kayak Flights results
    print_structured_result(google_flights_run_result)
    print_structured_result(kayak_flights_run_result)

if __name__ == "__main__":
    asyncio.run(main())
