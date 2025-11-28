from dotenv import load_dotenv
from agent import Agent

# Load environment variables from .env file
load_dotenv()


agent = Agent(model="gemini-3-pro-preview")
response1 = agent.run(
    contents="Hello, What are top 3 cities in Germany to visit? Only return the names of the cities."
)

print(f"Model: {response1.text}")
# Output: Berlin, Munich, Cologne
response2 = agent.run(
    contents="Tell me something about the second city."
)

print(f"Model: {response2.text}")


# Output: Munich is the capital of Bavaria and is known for its Oktoberfest.

def main():
    print("Hello from hello-genai!")


if __name__ == "__main__":
    main()
