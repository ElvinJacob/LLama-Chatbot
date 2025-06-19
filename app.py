# app.py

import streamlit as st
import google.generativeai as genai
import os

# Configure the Google Generative AI client with your API key
# For local development, you might still use dotenv if you prefer,
# but for Streamlit deployment, st.secrets is preferred.
# For simplicity and consistency with Streamlit's deployment model,
# we'll assume the API key is available via st.secrets.
# If running locally without st.secrets, ensure GOOGLE_API_KEY is in your environment.
try:
    # Use st.secrets if deployed on Streamlit Cloud, otherwise fall back to os.getenv
    # for local testing, assuming you've set it in your .env file and loaded it.
    # In a real deployed app, st.secrets is the way to go.
    api_key = st.secrets["GOOGLE_API_KEY"] if "GOOGLE_API_KEY" in st.secrets else os.getenv("GOOGLE_API_KEY")

    if not api_key:
        st.error("Google API Key not found. Please set it in .streamlit/secrets.toml or as an environment variable.")
        st.stop() # Stop the app if no API key is found

    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")
    st.info("Please ensure your Google API Key is correctly set in `.streamlit/secrets.toml` or as an environment variable.")
    st.stop() # Stop the app if configuration fails

# --- Model Initialization ---
# Ensure you use a model name that is actually available for generateContent
# You can uncomment the model listing logic below if you encounter a 404 error again
# to find the correct model name.
MODEL_NAME = 'gemini-1.5-flash' # Or 'gemini-pro', 'gemini-1.5-pro', based on your previous findings

try:
    model = genai.GenerativeModel(MODEL_NAME)
except Exception as e:
    st.error(f"Error initializing Gemini model '{MODEL_NAME}': {e}")
    st.info("Please check the model name, your network connection, or your API key's access.")
    # You might want to try listing models here for debugging:
    # st.write("Available models supporting 'generateContent':")
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         st.write(f"- {m.name}")
    st.stop()


# --- Streamlit App Interface ---
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini-Powered Chatbot")
st.write("Ask me anything! Type your message in the chat box below.")

# Initialize chat history in session state
# This is crucial for maintaining conversation across Streamlit reruns
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Optionally, add an initial greeting from the chatbot
    st.session_state.messages.append({"role": "assistant", "content": "Hello! How can I help you today?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Your message"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Gemini
    with st.spinner("Thinking..."): # Show a spinner while waiting for LLM
        try:
            # Prepare chat history for Gemini.
            # Gemini's `start_chat` expects a specific format for history.
            # We map our `st.session_state.messages` to that format.
            # The last message (current user prompt) is handled by send_message.
            # Make sure to exclude the current prompt from history when initializing the chat.
            # The 'role' for Gemini API is 'user' or 'model'.
            gemini_history = []
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    gemini_history.append({"role": "user", "parts": [msg["content"]]})
                elif msg["role"] == "assistant":
                    gemini_history.append({"role": "model", "parts": [msg["content"]]})

            # Start a chat session using the accumulated history
            chat = model.start_chat(history=gemini_history[:-1]) # Exclude the very last user prompt

            # Send the current user message
            response = chat.send_message(prompt)

            ai_response_text = ""
            for chunk in response:
                if hasattr(chunk, 'text'):
                    ai_response_text += chunk.text

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(ai_response_text.strip())

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": ai_response_text.strip()})

        except Exception as e:
            st.error(f"Error communicating with Gemini: {e}")
            st.info("Please check your internet connection, API key, and model availability. The conversation history might be out of sync.")
            # Optionally, remove the last user message if the response failed
            # st.session_state.messages.pop()
