import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "name": ["I'm a chatbot built with spaCy.", "You can call me NLPBot."],
    "weather": ["I can't give live weather updates yet, but it's always sunny in here!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase it?", "I didn't understand that."]
}

# Keywords associated with each intent
keywords = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "farewell", "later"],
    "thanks": ["thanks", "thank you", "appreciate"],
    "name": ["your name", "who are you", "what are you"],
    "weather": ["weather", "rain", "sunny", "forecast"]
}

import random

def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        for intent, keys in keywords.items():
            if token.text in keys:
                return intent
    return "default"

def chatbot():
    print("NLPBot: Hello! Ask me something (type 'exit' to quit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("NLPBot:", random.choice(responses["goodbye"]))
            break
        intent = get_intent(user_input)
        print("NLPBot:", random.choice(responses[intent]))

# Run the chatbot
if __name__ == "__main__":
    chatbot()
