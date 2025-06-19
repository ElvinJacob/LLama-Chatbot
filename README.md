Gemini-Powered Chatbot with Streamlit

A simple, interactive chatbot built with Python, leveraging the Google Gemini API for powerful conversational AI, and a user-friendly web interface powered by Streamlit.
🌟 Features

    Google Gemini Integration: Connects to the cutting-edge Gemini API for intelligent and context-aware responses.

    Streamlit Web Interface: Provides a clean, easy-to-use web-based chat application accessible via your browser.

    Session-based Chat History: Maintains conversation context within the Streamlit session for a natural chat experience.

    Secure API Key Handling: Utilizes Streamlit's secrets.toml for safe management of your API key, preventing it from being committed to version control.

🚀 Getting Started

Follow these steps to get your Gemini chatbot up and running on your local machine.
Prerequisites

Before you begin, ensure you have the following installed:

    Python 3.8+ (or higher)

    pip (Python package installer)

1. Clone the Repository

First, clone this GitHub repository to your local machine:

git clone https://github.com/ElvinJacob/LLama-Chatbot.git
cd LLama-Chatbot

(Replace ElvinJacob with your actual GitHub username if you forked it.)
2. Install Dependencies

Install the required Python libraries using pip:

pip install -r requirements.txt

(If you don't have a requirements.txt yet, create one with pip freeze > requirements.txt after installing streamlit, google-generativeai, and python-dotenv.)

Alternatively, install them manually if you haven't already:

pip install streamlit google-generativeai python-dotenv

3. Get Your Google Gemini API Key

    Go to Google AI Studio.

    Log in with your Google account.

    On the left sidebar, click "Get API key".

    Click "Create API key in new project" and copy the generated key.

4. Configure Your API Key

For security, your API key should not be hardcoded into your script or committed to Git. We'll use Streamlit's secrets management.

    Create a hidden directory named .streamlit in the root of your project:

    mkdir -p .streamlit

    Create a file named secrets.toml inside the .streamlit directory:

    nano .streamlit/secrets.toml

    Add your API key to this file in the following format:

    # .streamlit/secrets.toml
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"

    Replace "YOUR_GEMINI_API_KEY_HERE" with the actual API key you copied from Google AI Studio. Save and exit the file.

    Verify .gitignore: Ensure your .gitignore file (in the project root) contains these lines to prevent your secrets from being pushed to GitHub:

    .streamlit/secrets.toml
    .env

5. Run the Streamlit Application

Once everything is set up, you can run the chatbot application:

python3 -m streamlit run app.py

This command will start a local web server and open the chatbot interface in your default web browser (usually at http://localhost:8501).
💡 Usage

Simply type your message into the input box at the bottom of the Streamlit interface and press Enter. The chatbot will respond using the power of Google Gemini.
⚙️ Project Structure

LLama-Chatbot/
├── .streamlit/
│   └── secrets.toml  # Your Gemini API key (IGNORED by Git)
├── app.py            # The Streamlit web application for the chatbot
├── chatbot.py        # (Original) Command-line chatbot logic (can be removed or kept as reference)
├── .gitignore        # Specifies files and directories to ignore in Git
├── README.md         # This file!
└── requirements.txt  # List of Python dependencies (create with `pip freeze > requirements.txt`)

🛠️ Customization

    Change Gemini Model: In app.py, you can change the MODEL_NAME variable (e.g., 'gemini-pro', 'gemini-1.5-flash', 'gemini-1.5-pro') based on the models available to your API key. If you encounter a 404 error, temporarily uncomment the model listing loop in app.py to see available model names.

    Chatbot Persona: You can influence the chatbot's persona by adding initial messages to st.session_state.messages in app.py with the "assistant" role, or by using Gemini's system instructions feature if you upgrade your integration.

🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

    Fork the repository.

    Create a new branch (git checkout -b feature/your-feature-name).

    Make your changes.

    Commit your changes (git commit -m "Add new feature").

    Push to the branch (git push origin feature/your-feature-name).

    Open a Pull Request.

📄 License

This project is open-source and available under the MIT License (if you choose to add one).
🙏 Acknowledgments

    Google Gemini API for the powerful LLM capabilities.

    Streamlit for making web application development in Python incredibly simple and fast.
