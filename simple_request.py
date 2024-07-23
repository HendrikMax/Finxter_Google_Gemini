import os

import google.generativeai as genai
from dotenv import load_dotenv

from utils import safety_settings # import safety_settings from utils.py

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

GENERATION_CONFIG = {
    "temperature": 0.75,    # Creativity of the model. 0.0 is the most deterministic, 1.0 is the most creative.
    "top_p": 0.95,  # center on the most likely tokens - diversity of the model
    "top_k": 64,   # top-k sampling () - diversity of the model
    "max_output_tokens": 8192,  # maximum number of tokens to generate
    "response_mime_type": "text/plain", # json also available
}


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings.low,    # safety settings from utils.py
    generation_config=GENERATION_CONFIG,  # type: ignore
    system_instruction="You are a highly sarcastic and overly intellectual professor. You are helpful and do provide useful information but you are sarcastic and use overly complex language to show off your intellectual prowess and vocabulary.",
)


history = []    # chat history

chat_session = model.start_chat(history=history)    # start chat session with history


if __name__ == "__main__":
    query = input("Please ask a question: ")
    response = chat_session.send_message(query)

    print(f"\033[1;31m Text:\n{response.text}\033[0m")  # print the response
    print(f"\033[1;32m Candidates:\n{response.candidates}\033[0m") # print the candidates (If the model is unsure about the response, it will provide multiple candidates)
    print(f"\033[1;33m Usage metadata:\n{response.usage_metadata}\033[0m") # print the usage metadata (e.g. how many tokens were used, how many tokens were left, etc.)