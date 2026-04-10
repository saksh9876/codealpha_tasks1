def chatbot_response(user_input):
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I am a simple chatbot."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

while True:
    user_input = input("You: ").lower()
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input == "bye":
        break