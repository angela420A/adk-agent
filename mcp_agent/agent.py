import os

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

from . import config, prompt

CONFIG = config.Config("config.yaml")

google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY", "")
if not google_maps_api_key:
    print("WARNING: GOOGLE_MAPS_API_KEY is not set. Please set it as an environment variable or in the script.")

root_agent = LlmAgent(
    model=CONFIG.get("GEMINI", "MODEL"),
    name='maps_assistant_agent',
    instruction=prompt.MCP_AGENT_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "-y",
                    "@modelcontextprotocol/server-google-maps",
                ],
                env={
                    "GOOGLE_MAPS_API_KEY": google_maps_api_key
                }
            )
        )
    ],
)
