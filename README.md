# Hello GenAI

A scalable multi-agent architecture demonstrating Google's GenAI (Gemini) capabilities.

## Quick Start

1. Set up your environment:
   ```bash
   uv sync
   ```

2. Configure your API key:
   ```bash
   cd agents/file_agent
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. Run the example:
   ```bash
   uv run main.py
   ```

## Architecture

This project uses a modular architecture with three main components:

- **`adk/`** - Agent Development Kit: Core components for building agents
- **`tools/`** - Reusable tools that agents can use
- **`agents/`** - Individual agent implementations with their own configurations

## Usage

```python
from agents import FileAgent

agent = FileAgent()
response = agent.run("What files are here?")
print(response.text)
```

