import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

def process_text_prompt(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    prompt = "Generate a 2D layout of a 20m x 30m road with sidewalks."
    print(process_text_prompt(prompt))
