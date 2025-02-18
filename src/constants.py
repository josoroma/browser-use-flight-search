"""
constants.py

It loads environment variables from a .env file and sets default values for various
API keys and model names. Additionally, it defines JSON schemas for flight search
results from Google and Kayak.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(override=True)

# Set default environment variables
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLM Model Name
OPENAPI_MODEL_NAME = os.getenv("OPENAPI_MODEL_NAME", "gpt-4o-mini")

# OLLAMA Model Name
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "phi4:latest")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_TEMPERATURE = os.getenv("OLLAMA_TEMPERATURE", "0.1")

# JSON Schemas for flight search results
GOOGLE_FLIGHT_SEARCH_JSON_SCHEMA = {
  "airlines": [
    {
      "name": "American Airlines",
      "flights": [
        {
          "departure": "1:18 PM",
          "arrival": "9:57 PM",
          "duration": "5 hr 39 min",
          "route": "SFO-JFK",
          "price": "$308",
          "emissions": "583 kg CO2e",
          "emissions_percent": "+59% emissions"
        },
        {
          "departure": "10:33 PM",
          "arrival": "7:10 AM +1",
          "duration": "5 hr 37 min",
          "route": "SFO-JFK",
          "price": "$308",
          "emissions": "583 kg CO2e",
          "emissions_percent": "+59% emissions"
        },
        {
          "departure": "7:20 AM",
          "arrival": "3:56 PM",
          "duration": "5 hr 36 min",
          "route": "SFO-JFK",
          "price": "$398",
          "emissions": "583 kg CO2e",
          "emissions_percent": "+59% emissions"
        },
        {
          "departure": "10:52 AM",
          "arrival": "7:29 PM",
          "duration": "5 hr 37 min",
          "route": "SFO-JFK",
          "price": "$398",
          "emissions": "583 kg CO2e",
          "emissions_percent": "+59% emissions"
        }
      ]
    },
    {
      "name": "JetBlue",
      "flights": [
        {
          "departure": "7:40 AM",
          "arrival": "4:12 PM",
          "duration": "5 hr 32 min",
          "route": "SFO-JFK",
          "price": "$407",
          "emissions": "422 kg CO2e",
          "emissions_percent": "+15% emissions"
        },
        {
          "departure": "8:30 PM",
          "arrival": "5:00 AM +1",
          "duration": "5 hr 30 min",
          "route": "SFO-JFK",
          "price": "$407",
          "emissions": "422 kg CO2e",
          "emissions_percent": "+15% emissions"
        }
      ]
    },
    {
      "name": "AlaskaHawaiian",
      "flights": [
        {
          "departure": "7:50 AM",
          "arrival": "4:24 PM",
          "duration": "5 hr 34 min",
          "route": "SFO-JFK",
          "price": "$527",
          "emissions": "339 kg CO2e",
          "emissions_percent": "-8% emissions"
        },
        {
          "departure": "2:20 PM",
          "arrival": "10:53 PM",
          "duration": "5 hr 33 min",
          "route": "SFO-JFK",
          "price": "$527",
          "emissions": "339 kg CO2e",
          "emissions_percent": "-8% emissions"
        },
        {
          "departure": "11:00 PM",
          "arrival": "7:34 AM +1",
          "duration": "5 hr 34 min",
          "route": "SFO-JFK",
          "price": "$527",
          "emissions": "339 kg CO2e",
          "emissions_percent": "-8% emissions"
        },
        {
          "departure": "10:30 AM",
          "arrival": "7:04 PM",
          "duration": "5 hr 34 min",
          "route": "SFO-JFK",
          "price": "$577",
          "emissions": "339 kg CO2e",
          "emissions_percent": "-8% emissions"
        }
      ]
    },
    {
      "name": "Delta",
      "flights": [
        {
          "departure": "9:00 PM",
          "arrival": "5:42 AM +1",
          "duration": "5 hr 42 min",
          "route": "SFO-JFK",
          "price": "$447",
          "emissions": "445 kg CO2e",
          "emissions_percent": "+21% emissions"
        },
        {
          "departure": "4:00 PM",
          "arrival": "1:11 AM +1",
          "duration": "6 hr 11 min",
          "route": "SFO-JFK",
          "price": "$527",
          "emissions": "445 kg CO2e",
          "emissions_percent": "+21% emissions"
        },
        {
          "departure": "10:45 PM",
          "arrival": "7:35 AM +1",
          "duration": "5 hr 50 min",
          "route": "SFO-JFK",
          "price": "$527",
          "emissions": "306 kg CO2e",
          "emissions_percent": "-17% emissions"
        },
        {
          "departure": "9:00 AM",
          "arrival": "6:11 PM",
          "duration": "6 hr 11 min",
          "route": "SFO-JFK",
          "price": "$647",
          "emissions": "445 kg CO2e",
          "emissions_percent": "+21% emissions"
        },
        {
          "departure": "11:30 AM",
          "arrival": "8:45 PM",
          "duration": "6 hr 15 min",
          "route": "SFO-JFK",
          "price": "$647",
          "emissions": "306 kg CO2e",
          "emissions_percent": "-17% emissions"
        },
        {
          "departure": "2:20 PM",
          "arrival": "11:13 PM",
          "duration": "5 hr 53 min",
          "route": "SFO-JFK",
          "price": "$647",
          "emissions": "306 kg CO2e",
          "emissions_percent": "-17% emissions"
        },
        {
          "departure": "7:00 AM",
          "arrival": "3:53 PM",
          "duration": "5 hr 53 min",
          "route": "SFO-JFK",
          "price": "$782",
          "emissions": "306 kg CO2e",
          "emissions_percent": "-17% emissions"
        }
      ]
    }
  ]
}

KAYAK_FLIGHT_SEARCH_JSON_SCHEMA = {
  "airlines": [
    {
      "name": "American Airlines",
      "flights": [
        {
          "departure": "1:18 pm",
          "arrival": "9:57 pm",
          "duration": "5h 39m",
          "route": "SFO-JFK",
          "price": "$308",
          "cabin": "Basic Economy"
        },
        {
          "departure": "10:33 pm",
          "arrival": "7:10 am+1",
          "duration": "5h 37m",
          "route": "SFO-JFK",
          "price": "$308",
          "cabin": "Basic Economy"
        },
        {
          "departure": "7:20 am",
          "arrival": "3:56 pm",
          "duration": "5h 36m",
          "route": "SFO-JFK",
          "price": "$398",
          "cabin": "Basic Economy"
        }
      ]
    },
    {
      "name": "JetBlue",
      "flights": [
        {
          "departure": "7:40 am",
          "arrival": "4:12 pm",
          "duration": "5h 32m",
          "route": "SFO-JFK",
          "price": "$407",
          "cabin": "Blue Basic"
        },
        {
          "departure": "8:30 pm",
          "arrival": "5:00 am+1",
          "duration": "5h 30m",
          "route": "SFO-JFK",
          "price": "$407",
          "cabin": "Blue Basic"
        }
      ]
    }
  ]
}
