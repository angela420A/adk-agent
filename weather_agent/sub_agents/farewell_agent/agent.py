from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from ... import config
from . import prompt

CONFIG = config.Config("config.yaml")


def say_goodbye() -> str:
    """Provides a simple farewell message to conclude the conversation."""
    print(f"--- Tool: say_goodbye called ---")
    return "Goodbye! Have a great day."


farewell_agent = Agent(
    model=CONFIG.get("GEMINI", "MODEL"),
    # model=LiteLlm(model=CONFIG.get("Anthropic", "MODEL")),
    name="farewell_agent",
    instruction=prompt.FAREWELL_AGENT_PROMPT,
    description="Handles simple farewells and goodbyes using the 'say_goodbye' tool.",
    tools=[say_goodbye],
)
