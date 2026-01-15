import os
from dotenv import load_dotenv


class AgentConfiguration:
    """Configuration class for agent settings.

    Loads environment variables and provides access to configuration values
    as attributes.

    Attributes:
        api_key: The Gemini API key from environment variables.
        model: The Gemini model identifier to use.

    Raises:
        ValueError: If GEMINI_API_KEY is not set in environment variables.
    """

    def __init__(self):
        """Initialize the configuration by loading environment variables."""
        # Load environment variables from .env file
        load_dotenv()

        # Get API key with validation
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables. "
                "Please set it in your .env file. "
                "Get your API key from: https://aistudio.google.com/api-keys"
            )
        self.api_key = api_key

        # Get model with default fallback
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


# Create a singleton instance for easy import
agent_configuration = AgentConfiguration()
