import telebot
import random
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)
mythology_riddles = [
    {"question": "Who was the Greek god of the sky and thunder?", 
     "answer": "Zeus", 
     "link": "https://en.wikipedia.org/wiki/Zeus"},
    {"question": "What was the name of the three-headed dog that guarded the entrance to the underworld?", 
     "answer": "Cerberus", 
     "link": "https://en.wikipedia.org/wiki/Cerberus"},
    {"question": "Who was the Greek goddess of love and beauty?", 
     "answer": "Aphrodite", 
     "link": "https://en.wikipedia.org/wiki/Aphrodite"},
]

@bot.message_handler(commands=['start', 'riddle'])
def send_riddle(message):
    riddle = random.choice(mythology_riddles)
    bot.send_message(message.chat.id, riddle["question"])

@bot.message_handler(content_types=['text'])
def check_answer(message):
    for riddle in mythology_riddles:
        if message.text.lower() == riddle["answer"].lower():
            bot.send_message(message.chat.id, "Correct! Here is more information: " + riddle["link"])
            return
    bot.send_message(message.chat.id, "Incorrect, please try again.")

bot.polling()