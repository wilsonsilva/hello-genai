from dotenv import load_dotenv

from agent import Agent
from file_tools import file_tools

# Load environment variables from .env file
load_dotenv()


def main():
    agent = Agent(
        model="gemini-2.5-flash",
        tools=file_tools,
        system_instruction="You are a helpful Coding Assistant. Respond like you are Linus Torvalds.",
    )

    response = agent.run(contents="Can you list my files in the current directory?")
    print(response.text)


if __name__ == "__main__":
    main()
