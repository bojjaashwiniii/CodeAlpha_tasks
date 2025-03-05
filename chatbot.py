import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# First, download necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there!", "Hey! How can I assist you?"]),
    (r"what is your name?", ["I'm a chatbot, but you can call me ChatBot.", "My name is ChatBot."]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm doing well, how about you?"]),
    (r"what time is it?", ["I don't have access to real-time data right now, but you can check the clock!"]),
    (r"quit", ["Goodbye!", "See you later!"]),
    (r"(.*) your name?", ["My name is ChatBot.", "I go by ChatBot."]),
    (r"(.*) (good|great|awesome|okay|fine)", ["I'm glad to hear you're doing well!"]),
    (r"(.*)", ["Sorry, I didn't understand that.", "Can you please rephrase your question?"])
]

# Create a ChatBot class using the patterns
class SimpleChatBot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)
    
    def chat(self):
        print("Hello! I am your chatbot. Type 'quit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                print("ChatBot: Goodbye!")
                break
            else:
                response = self.chatbot.respond(user_input)
                print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot = SimpleChatBot()
    chatbot.chat()
