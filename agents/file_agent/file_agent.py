"""File Agent - An agent specialized in file system operations."""

from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from this agent's directory BEFORE importing Agent
# This ensures the API key is available when agent_configuration is initialized
agent_dir = Path(__file__).parent
env_path = agent_dir / ".env"

if env_path.exists():
    load_dotenv(env_path)

from adk import Agent  # noqa: E402
from tools import file_tools  # noqa: E402


class FileAgent(Agent):
    """An agent specialized in file system operations.

    This agent inherits from the base Agent class and is pre-configured
    with file system tools and appropriate instructions.
    """

    def __init__(self, model: str = None):
        """Initialize the file agent.

        Args:
            model: Optional model identifier. If not provided, uses default from config.
        """
        system_instruction = """You are a helpful file management assistant.
You have access to tools for reading, writing, and listing files.
Always be careful when writing files - make sure you understand the context first.
When asked to work with files, use the appropriate tools."""

        super().__init__(
            model=model,
            tools=file_tools,
            system_instruction=system_instruction,
        )
