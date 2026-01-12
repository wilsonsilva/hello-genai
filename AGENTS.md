# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

## Project Overview

This is a Python demonstration project for Google's GenAI (Gemini) API. The project showcases a conversational agent that maintains context across multiple interactions using the `google-genai` library.

## Environment Setup

**Package Manager**: This project uses `uv` (not pip or poetry).

**Python Version**: 3.14 (managed via `.python-version`)

**Environment Variables**: Copy `.env.example` to `.env` and add your Gemini API key from https://aistudio.google.com/api-keys

```bash
cp .env.example .env
# Then edit .env to add your GEMINI_API_KEY
```

## Development Commands

### Setup and Installation
```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate
```

### Running the Application
```bash
# Run the main script
uv run main.py

# Or with activated venv
python main.py
```

### Adding Dependencies
```bash
# Add a new dependency
uv add <package-name>

# Add a dev dependency
uv add --dev <package-name>
```

### Code Quality Tools
```bash
# Format code with black
uv run black .

# Lint code with ruff
uv run ruff check .

# Auto-fix linting issues
uv run ruff check --fix .
```

### Running Examples
```bash
# Run the main script (demonstrates basic agent with function calling)
uv run main.py

# Run comprehensive examples with multiple tools
uv run example_with_tools.py
```

## Code Architecture

### Agent Class (`agent.py`)
The core `Agent` class provides:
- **Conversation History**: Maintains context in `self.contents` as a list of message dictionaries
- **Function Calling**: Supports tool execution via Google GenAI's native function calling
- **Recursive Tool Execution**: When the model requests a function call, the agent executes it and automatically sends results back

### Function Calling Flow
1. User message sent with tool declarations to the model
2. Model responds with text and/or function call requests
3. If function calls exist, they are executed locally and logged
4. Function results are sent back to the model (via recursive `run()` call)
5. Model generates final natural language response

### Tool Implementation (`file_tools.py`)
Tools are standard Python functions with:
- Type hints for parameters
- Docstrings describing functionality and arguments (used by the model)
- Optional `@log_function_call` decorator for debugging

The model automatically converts docstrings into function schemas for the API.

### Message Structure
Messages follow this format:
```python
{"role": "user", "parts": [{"text": "user message"}]}
```

Model responses are appended directly from `response.candidates[0].content`

## Important Notes

- The project uses **Gemini 2.5 Flash** model by default (`gemini-2.5-flash`)
- API key must be set as `GEMINI_API_KEY` environment variable
- The Agent class maintains conversational context automatically across multiple `run()` calls
- Function calls are logged to stdout with `[Function Call]` prefix when using the decorator
- No test suite currently exists in this project
