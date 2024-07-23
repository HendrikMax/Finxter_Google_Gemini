# puts the import an API-Keys in a function and returns the genai object. This way, the API key is only loaded once and the genai object is returned to the main script.

import os

import google.generativeai as genai
from dotenv import load_dotenv


def configure_genai():
    load_dotenv()
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    return genai