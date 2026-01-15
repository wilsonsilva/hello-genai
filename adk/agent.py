from google import genai
from google.genai import types
from .agent_configuration import agent_configuration


class Agent:
    def __init__(
        self,
        model: str = None,
        tools: list = None,
        system_instruction: str = "You are a helpful assistant.",
    ):
        """Initialize a conversational agent with Google GenAI.

        Args:
            model: The Gemini model identifier (e.g., "gemini-2.5-flash").
                   If not provided, uses the model from agent_configuration.
            tools: List of Python functions to use as tools
            system_instruction: System prompt that defines agent behavior

        Examples:
            Basic initialization:

            >>> agent = Agent(
            ...     model="gemini-2.5-flash",
            ...     system_instruction="You are a helpful assistant."
            ... )

            With tools:

            >>> def read_file(file_path: str) -> str:
            ...     '''Reads a file and returns its contents.
            ...
            ...     Args:
            ...         file_path: Path to the file to read.
            ...     '''
            ...     with open(file_path, "r") as f:
            ...         return f.read()
            ...
            >>> agent = Agent(
            ...     model="gemini-2.5-flash",
            ...     tools=[read_file],
            ...     system_instruction="You are a helpful Coding Assistant."
            ... )
        """
        self.model = model or agent_configuration.model
        self.client = genai.Client(api_key=agent_configuration.api_key)
        self.contents = []
        self.tools = tools or []
        self.system_instruction = system_instruction

    def run(self, contents: str | list[dict[str, str]]):
        """Execute a conversational turn with the agent.

        This method sends a message to the agent and returns the response.
        It automatically maintains the conversation history and handles function calls
        by recursively calling itself when the model requests tool execution.

        The function calling flow:
        1. User message is sent with available tool declarations
        2. Model responds with text and/or function calls
        3. If function calls exist, they are executed locally
        4. Function results are sent back to the model (recursive call)
        5. Model generates a final natural language response

        Args:
            contents: Either a string message or a list of part dictionaries
                     for continuing a conversation with function responses

        Returns:
            The model's response object containing the generated content

        Examples:
            Basic query with automatic function calling:

            >>> from file_tools import file_tools
            >>> agent = Agent(
            ...     model="gemini-2.5-flash",
            ...     tools=file_tools,
            ...     system_instruction="You are a helpful Coding Assistant."
            ... )
            >>> response = agent.run("Can you list my files in the current directory?")
            [Function Call] name: "list_dir" args { fields { key: "directory_path" value { string_value: "." } } }
            [Function Response] {'result': ['WARP.md', 'README.md', 'main.py', 'agent.py', ...]}
            >>> print(response.text)
            There you have it. A directory full of... WARP.md, README.md, and a bunch of other junk.

            The conversation is maintained across multiple calls:

            >>> response2 = agent.run("Can you read the README.md file?")
            [Function Call] name: "read_file" args { fields { key: "file_path" value { string_value: "README.md" } } }
            [Function Response] {'result': '# hello-genai\n\nDemonstration project...'}
            >>> print(response2.text)
            Alright, here's what's in your README.md...
        """
        if isinstance(contents, list):
            # Append a part to an existing conversation
            self.contents.append({"role": "user", "parts": contents})
        else:
            # Start a new conversation
            self.contents.append({"role": "user", "parts": [{"text": contents}]})

        # Configure the client and tools
        config = types.GenerateContentConfig(
            system_instruction=self.system_instruction,
            tools=self.tools,
        )

        # Send request with function declarations
        response = self.client.models.generate_content(
            model=self.model, contents=self.contents, config=config
        )
        self.contents.append(response.candidates[0].content)

        return response
