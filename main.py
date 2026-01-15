from agents import FileAgent

# Create the file agent
agent = FileAgent()

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
