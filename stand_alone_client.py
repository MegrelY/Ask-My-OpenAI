from openai import OpenAI
import os

# Set up the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to generate a response using GPT-4o
def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
user_prompt = "What are the main differences between Python 2 and Python 3?"
result = generate_response(user_prompt)
print(result)