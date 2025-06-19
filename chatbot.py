import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI client with your API key
try:
    gemini_api_key = os.getenv("GOOGLE_API_KEY")
    if not gemini_api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file or environment variables.")
    genai.configure(api_key=gemini_api_key)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    print("Please ensure your GOOGLE_API_KEY is correctly set in your .env file.")
    exit() # Exit if API key is not configured correctly

# --- TEMPORARY: LIST AVAILABLE MODELS (RUN ONCE, THEN REMOVE/COMMENT OUT) ---
print("\n--- Listing available Gemini models supporting 'generateContent' ---")
found_preferred_model = False
available_model_name = None

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"  - {m.name}")
        # Prioritize widely used models. Adjust this logic based on your desired model.
        if m.name == 'models/gemini-1.5-flash' or m.name == 'models/gemini-pro': # Try these first
            if not available_model_name: # Only set if a better one hasn't been found
                 available_model_name = m.name
            if m.name == 'models/gemini-1.5-flash': # Prefer 1.5-flash if available
                available_model_name = m.name
                found_preferred_model = True
        elif not found_preferred_model and 'gemini' in m.name and 'preview' not in m.name:
            # Fallback to other non-preview Gemini models if preferred not found
            available_model_name = m.name

print("------------------------------------------------------------------\n")

if not available_model_name:
    print("Error: No suitable Gemini model found that supports 'generateContent'.")
    print("Please check Google AI Studio for available models in your region and ensure billing is enabled (even for free tier).")
    exit()

# Initialize the Gemini model with the name found from the list, or a default if not found
# After you run the script once and see the list, you should REPLACE 'available_model_name'
# with the exact model name you want to use (e.g., 'models/gemini-1.5-flash')
# and then COMMENT OUT the model listing block above.
try:
    model = genai.GenerativeModel(available_model_name)
    print(f"Using Gemini model: {available_model_name}")
except Exception as e:
    print(f"Error initializing Gemini model '{available_model_name}': {e}")
    print("This might indicate a problem with the model name, region, or API key access.")
    exit()

def chatbot():
    print("\nHello! I'm an LLM-powered chatbot, now powered by Google Gemini!")
    print("You can type 'quit' to exit.")

    # Start a new chat session with the model.
    # Gemini's `start_chat` handles history internally.
    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! It was nice chatting with you.")
            break

        try:
            # Send the user's message to the Gemini model.
            # The send_message method automatically appends to and uses the chat history.
            response = chat.send_message(user_input)

            # Extract the AI's response text.
            # The response might come in chunks, so we iterate to get all text.
            ai_response_text = ""
            for chunk in response:
                if hasattr(chunk, 'text'):
                    ai_response_text += chunk.text

            print(f"Chatbot: {ai_response_text.strip()}")

        except Exception as e:
            print(f"Chatbot: Oops! Something went wrong communicating with the LLM: {e}")
            print("Chatbot: Please check your internet connection, the chosen model's availability, API key, and free tier quota.")
            # If an error occurs, the model's internal history might be out of sync
            # or the current turn failed. For robust error handling in a real app,
            # you might decide to clear `chat.history` or implement retry logic.

if __name__ == "__main__":
    chatbot()
