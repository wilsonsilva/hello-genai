from google import genai


class Agent:
    def __init__(self, model: str):
        self.model = model
        self.client = genai.Client()
        self.contents = []

    def run(self, contents: str):
        self.contents.append({"role": "user", "parts": [{"text": contents}]})

        response = self.client.models.generate_content(model=self.model, contents=self.contents)
        self.contents.append(response.candidates[0].content)

        return response
