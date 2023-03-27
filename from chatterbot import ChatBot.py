from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from textblob import TextBlob

# Create a new chatbot
chatbot = ChatBot('Emotional Bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the english corpus
trainer.train("chatterbot.corpus.english")

# Define a function to get the sentiment of a message
def get_sentiment(message):
    blob = TextBlob(message)
    return blob.sentiment.polarity

# Define a function to get the emotional response of a message
def get_emotional_response(message):
    sentiment = get_sentiment(message)
    if sentiment > 0.5:
        return "I'm so happy to hear that!"
    elif sentiment > 0:
        return "That's great!"
    elif sentiment == 0:
        return "I don't know how to respond to that."
    elif sentiment > -0.5:
        return "I'm sorry to hear that."
    else:
        return "That's terrible. I'm here for you."

# Define a function to get the bot's response
def get_bot_response(message):
    emotional_response = get_emotional_response(message)
    response = chatbot.get_response(message)
    return emotional_response + ' ' + str(response)

# Start the conversation
print('Emotional Bot: Hi, how can I help you today?')
while True:
    message = input('You: ')
    if message.strip() == 'bye':
        print('Emotional Bot: Bye!')
        break
    else:
        response = get_bot_response(message)
        print('Emotional Bot:', response)
