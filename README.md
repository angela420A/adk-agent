# ADK Agent

A modular Python project for building conversational AI agents using [Google ADK](https://pypi.org/project/google-adk/). This repository demonstrates a weather assistant and a maps assistant, each with sub-agents for greetings and farewells.

## Features

- **Weather Agent**: Answers weather queries for specific cities using mock data.
  - **Greeting Agent**: Provides friendly greetings.
  - **Farewell Agent**: Handles polite goodbyes.
- **MCP Agent**: Assists with mapping, directions, and finding places using Google Maps tools.
- Modular configuration via YAML files.
- Easily extensible with new tools and sub-agents.

## Project Structure

## Setup

1. **Python Version**: Requires Python 3.13+  
   (See [.python-version](.python-version))

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables (for MCP Agent)**:
    - Obtain a Google Maps API key.
    - Set it in your environment:
    ```
    export GOOGLE_MAPS_API_KEY=your_api_key_here
    ```

## Configuration
Each agent reads its settings from a `config.yaml` file.
You can change the underlying LLM model by editing the `MODEL` fields in the YAML.

## Extending
Add new tools by defining Python functions and including them in the agent's tools list.
Add new `sub-agents` by creating a new folder under `weather_agent/sub_agents/` or `mcp_agent/sub_agents/` and following the existing pattern.
