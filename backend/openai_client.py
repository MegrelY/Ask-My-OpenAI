import openai
import os
from backend.config import settings
from backend.logger import logger


# Initialize OpenAI client
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to generate a response using GPT-4o
def generate_response(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7  # Adjust this parameter to control randomness
        )
        return response.choices[0].message.content.strip()  # Extract the response content
    except Exception as e:
        logger.error(f"Error in generate_response: {e}")
        return f"An error occurred: {str(e)}"

