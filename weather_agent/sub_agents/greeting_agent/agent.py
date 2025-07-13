from typing import Optional

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from ... import config
from . import prompt

CONFIG = config.Config("config.yaml")


def say_hello(name: Optional[str] = None) -> str:
    """Provides a simple greeting. If a name is provided, it will be used.

    Args:
        name (str, optional): The name of the person to greet. Defaults to a generic greeting if not provided.

    Returns:
        str: A friendly greeting message.
    """
    if name:
        greeting = f"Hello, {name}!"
        print(f"--- Tool: say_hello called with name: {name} ---")
    else:
        greeting = "Hello there!"
        print(
            f"--- Tool: say_hello called without a specific name (name_arg_value: {name}) ---")
    return greeting


greeting_agent = Agent(
    model=CONFIG.get("GEMINI", "MODEL"),
    # model=LiteLlm(model=CONFIG.get("OPRNAI", "MODEL")),
    name="greeting_agent",
    instruction=prompt.GREETING_AGENT_PROMPT,
    description="Handles simple greetings and hellos using the 'say_hello' tool.",
    tools=[say_hello],
)
