# Agent Development Kit (ADK)

Core components for building AI agents with Google GenAI.

## Components

### Agent (`agent.py`)

The main Agent class provides:

- **Conversation History**: Automatically maintains context across multiple interactions
- **Function Calling**: Supports tool execution via GenAI's native function calling
- **Recursive Tool Execution**: Automatically handles function call requests and responses

#### Usage

```python
from adk import Agent

# Create an agent
agent = Agent(
    model="gemini-2.5-flash",  # Optional, defaults from config
    tools=[tool1, tool2],      # Optional list of functions
    system_instruction="You are a helpful assistant."
)

# Run a query
response = agent.run("Your question here")
print(response.text)

# Conversation is maintained
response2 = agent.run("Follow-up question")
```

### AgentConfiguration (`agent_configuration.py`)

Manages environment variables and configuration:

```python
from adk import AgentConfiguration

# Load from default .env location
config = AgentConfiguration()
print(config.api_key)
print(config.model)

# Load from specific .env file
config = AgentConfiguration(env_path="/path/to/.env")
```

#### Environment Variables

- `GEMINI_API_KEY` - Required. Your Gemini API key
- `GEMINI_MODEL` - Optional. Defaults to "gemini-2.5-flash"

## Function Calling Flow

1. User message sent with tool declarations
2. Model responds with text and/or function calls
3. If function calls exist, they're executed locally
4. Function results sent back to model (recursive call)
5. Model generates final natural language response

## Example

```python
from adk import Agent

def get_weather(location: str) -> str:
    """Get the weather for a location.
    
    Args:
        location: The city name
    """
    return f"The weather in {location} is sunny"

agent = Agent(
    tools=[get_weather],
    system_instruction="You are a weather assistant."
)

response = agent.run("What's the weather in Tokyo?")
# Model will call get_weather("Tokyo") automatically
print(response.text)
```
