from load_env import configure_genai
from utils import safety_settings

genai = configure_genai()


character = input("What is your favorite movie character? (e.g. Gollum): ")
movie = input("What movie are they from? (e.g. Lord of the Rings): ")


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings.low, # safety settings from utils.py
    system_instruction=f"You are helpful and provide good information but you are {character} from {movie}. You will stay in character as {character} no matter what. Make sure you find some way to relate your responses to {character}'s personality or the movie {movie} at least once every response.",
)

history = []

chat_session = model.start_chat(history=history)


if __name__ == "__main__":
    try:
        while True:
            query = input("\nPlease ask a question or use CTRL+C to exit: ")

# Part 1: model - external History

            # response = chat_session.send_message(query)
            # print(f"\033[1;34m{response.text}\033[0m")
            # history.append(
            #     {
            #         "role": "user",
            #         "parts": [query],
            #     }
            # )
            # history.append(
            #     {
            #         "role": "model",
            #         "parts": [response.text],
            #     }
            # )
            # for message in history:
            #     print(f"{message}")


# Part 2: model - internal history with stream output

            response = chat_session.send_message(query, stream=True)
            for chunk in response:
                if chunk.candidates[0].finish_reason == 3:   # finish_reason 3 means the model is unsure about the response (see API documentation)
                    print(f"\n\033[1;31mPlease ask a more appropriate question!\033[0m", end="")    # print the response in blue color (\033[1;31m)                  
                    chat_session.rewind() # rewind the chat session to the last message (delete the last message from history  )
                    break  # break the loop to while() and ask for a new question
                print(f"\033[1;34m{chunk.text}\033[0m", end="")
            print("\n")

            # for message in chat_session.history:  # print the internal chat history from the model
            #   print(f"{message}")


    except KeyboardInterrupt:
        print("Shutting down...")