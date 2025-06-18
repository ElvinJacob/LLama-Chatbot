print("Hello! I'm a simple chatbot. You can type 'quit' to exit.")

while True:
    user_input = input("You: ").lower() # Get user input and convert to lowercase

    if user_input == 'quit':
        print("Chatbot: Goodbye! It was nice chatting with you.")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hi there! How can I help you today?")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a program, so I don't have feelings, but I'm ready to chat!")
    elif "what is your name" in user_input:
        print("Chatbot: I don't have a name. You can call me Chatbot.")
    elif "help" in user_input:
        print("Chatbot: I can answer basic questions or just chat. Try asking me something!")
    elif "weather" in user_input:
        print("Chatbot: I cannot provide real-time weather information.")
    elif "time" in user_input:
        print("Chatbot: I do not have access to the current time.")
    elif "thank you" in user_input or "thanks" in user_input:
        print("Chatbot: You're welcome!")
    else:
        print("Chatbot: I'm not sure how to respond to that. Can you rephrase or ask something else?")

if __name__ == "__main__":
    def chatbot():
        # Your chatbot logic here (same as above)
        print("Hello! I'm a simple chatbot. You can type 'quit' to exit.")

        while True:
            user_input = input("You: ").lower() # Get user input and convert to lowercase

            if user_input == 'quit':
                print("Chatbot: Goodbye! It was nice chatting with you.")
                break
            elif "hello" in user_input or "hi" in user_input:
                print("Chatbot: Hi there! How can I help you today?")
            elif "how are you" in user_input:
                print("Chatbot: I'm just a program, so I don't have feelings, but I'm ready to chat!")
            elif "what is your name" in user_input:
                print("Chatbot: I don't have a name. You can call me Chatbot.")
            elif "help" in user_input:
                print("Chatbot: I can answer basic questions or just chat. Try asking me something!")
            elif "weather" in user_input:
                print("Chatbot: I cannot provide real-time weather information.")
            elif "time" in user_input:
                print("Chatbot: I do not have access to the current time.")
            elif "thank you" in user_input or "thanks" in user_input:
                print("Chatbot: You're welcome!")
            else:
                print("Chatbot: I'm not sure how to respond to that. Can you rephrase or ask something else?")
    chatbot() # Call the chatbot function
