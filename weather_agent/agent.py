import asyncio
import logging
import os
import warnings

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm  # For multi-model support
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from . import config, prompt
from .sub_agents.farewell_agent import farewell_agent
from .sub_agents.greeting_agent import greeting_agent

# Ignore all warnings
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

CONFIG = config.Config("config.yaml")


# Tools
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city (e.g., "New York", "London", "Tokyo").

    Returns:
        dict: A dictionary containing the weather information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'report' key with weather details.
              If 'error', includes an 'error_message' key.
    """
    print(
        # Log tool execution
        f"--- Tool: get_weather called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "")  # Basic normalization

    # Mock weather data
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"Sorry, I don't have weather information for '{city}'."}


# root_agent = Agent(
#     name="weather_agent_v1",
#     model=CONFIG.get("GEMINI", "MODEL"),
#     description="Provides weather information for specific cities.",
#     instruction=prompt.WEATHER_AGENT_PROMPT,
#     tools=[get_weather],
# )

root_agent = Agent(
    name="weather_agent_v1",
    model=CONFIG.get("GEMINI", "MODEL"),
    description="Provides weather information for specific cities.",
    instruction=prompt.WEATHER_AGENT_PROMPT,
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent],
)
