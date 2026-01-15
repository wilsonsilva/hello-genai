from dotenv import load_dotenv
from agent import Agent
from file_tools import file_tools

# Load environment variables from .env file
load_dotenv()

# Create an agent with file system tools
system_instruction = """You are a helpful file management assistant.
You have access to tools for reading, writing, and listing files.
Always be careful when writing files - make sure you understand the context first.
When asked to work with files, use the appropriate tools."""

agent = Agent(
    model="gemini-2.5-flash",
    tools=file_tools,
    system_instruction=system_instruction,
)

# Example 1: List files in the current directory
print("=" * 80)
print("Example 1: List files in current directory")
print("=" * 80)
response1 = agent.run("What files are in the current directory?")
print(f"Agent: {response1.text}")

# Example 2: Read a specific file
print("\n" + "=" * 80)
print("Example 2: Read agent.py file")
print("=" * 80)
response2 = agent.run("Can you read the agent.py file and tell me what it does?")
print(f"Agent: {response2.text}")

# Example 3: Create a new file
print("\n" + "=" * 80)
print("Example 3: Create a new file")
print("=" * 80)
response3 = agent.run(
    "Create a file called test_output.txt with the content 'Hello from the agent!'"
)
print(f"Agent: {response3.text}")

# Example 4: Complex multi-tool task
print("\n" + "=" * 80)
print("Example 4: Complex multi-tool task")
print("=" * 80)
response4 = agent.run(
    "Read the README.md file if it exists, and create a summary.txt file with a brief summary of its contents"
)
print(f"Agent: {response4.text}")
