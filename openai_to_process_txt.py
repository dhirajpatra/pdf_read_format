import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the API_KEY value
api_key = os.getenv("API_KEY")


# Function to format text using GPT-3
def format_text(text):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=2000,  # Adjust max tokens as needed
        temperature=0.7,  # Adjust temperature for creativity
    )
    formatted_text = response.choices[0].text
    return formatted_text

