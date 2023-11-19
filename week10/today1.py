import random

# Pre-defined responses for the chatbot
responses = {
    "Hello": "Hi there! How can I help you today?",
    "What's the traffic update in Lahore right now?": "I'm sorry, I don't have access to real-time map information.",
    "Tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "Tell me a story": "Once upon a time, in a land far, far away..."
}

def chatbot_response(user_input):
    user_input = user_input.strip()
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm not sure how to respond to that."

# Main chat loop
print("Chatbot: Hi there! How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
