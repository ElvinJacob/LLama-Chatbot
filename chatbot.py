import os
from openai import OpenAI # For OpenAI API integration
from dotenv import load_dotenv # To load API key securely

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key
# The API key is loaded from the environment variable OPENAI_API_KEY
# If you don't use .env, you'd do client = OpenAI(api_key="YOUR_HARDCODED_KEY_HERE")
# But hardcoding is NOT recommended for security.
client = OpenAI()

def chatbot():
    print("Hello! I'm an LLM-powered chatbot. You can type 'quit' to exit.")
    print("I can now understand and generate more complex responses!")

    # Keep track of conversation history for better context
    messages = [
        {"role": "system", "content": "You are a helpful and friendly chatbot. Keep responses concise unless asked for details."}
    ]

    while True:
        user_input = input("You: ").strip() # Get user input and remove leading/trailing whitespace

        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! It was nice chatting with you.")
            break

        # Add user's message to history
        messages.append({"role": "user", "content": user_input})

        try:
            # Call the OpenAI API
            # model="gpt-3.5-turbo" is a good balance of cost and performance
            # You can also try "gpt-4o" for more advanced capabilities
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Extract the AI's response
            ai_response = completion.choices[0].message.content

            # Add AI's response to history
            messages.append({"role": "assistant", "content": ai_response})

            print(f"Chatbot: {ai_response}")

        except Exception as e:
            print(f"Chatbot: Oops! Something went wrong communicating with the LLM: {e}")
            print("Chatbot: Please check your internet connection and API key.")
            # If an error occurs, remove the last user message from history to avoid confusion
            messages.pop()

if __name__ == "__main__":
    chatbot()
