# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

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

## Code Architecture

### Agent Pattern
The core architecture uses an `Agent` class that:
- Maintains conversation history in `self.contents` as a list of message dictionaries
- Each message has a `role` ("user" or model response) and `parts` containing the text
- Automatically appends user queries and model responses to maintain context
- Uses the Google GenAI client for model interactions

### Message Structure
Messages follow this format:
```python
{"role": "user", "parts": [{"text": "user message"}]}
```

Model responses are appended directly from `response.candidates[0].content`

### Environment Configuration
- API keys loaded via `python-dotenv`
- `.env` file is git-ignored for security
- `.env.example` serves as a template

## Important Notes

- The project uses **Gemini 3 Pro Preview** model by default (`gemini-3-pro-preview`)
- API key must be set as `GEMINI_API_KEY` environment variable
- The Agent class maintains conversational context automatically across multiple `run()` calls
- No test suite currently exists in this project
