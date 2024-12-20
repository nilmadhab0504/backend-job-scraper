from openai import OpenAI

class LLMService:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def get_llm_result(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=1000,
                top_p=1,
            )

            # Parse the response content
            data = response.choices[0].message.content.strip()
            return data
        except Exception as e:
            return None