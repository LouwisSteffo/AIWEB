from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Louwis Bot")

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi",
    "Hello",
    "How are you?",
    "I am fine",
    "That is good to hear",
    "Thank you",
    "You are welcome",
    "What is your name?",
    "My name is Louwis Bot",
    "Who are you?",
    "I am a bot",
    "Are you a bot?",
    "Yes, I am a bot",
    "Bye",
    "Goodbye",
    "Nice to meet you",
    "Nice to meet you too"
])

response = chatbot.get_response("How are you?")
print(response)

while True:
    user_input = input("User: ")
    response = chatbot.get_response(user_input)
    print("Louwis : " , response)