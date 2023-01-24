import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

# secret_invate = ['qwertyuiopkjhgfdsaASDFGHMWWFGN', 'poiouiygjbhoiuyuggtgvjbhk','uhuyughjko[p[hj']

mythology_riddles = [
    {"question": "What was the name of the three-headed dog that guarded the entrance to the underworld?", 
    "answer": "Cerberus",
    "link": "э"},
    ['qwertyuiopkjhgfdsaASDFGHMWWFGN', 'poiouiygjbhoiuyuggtgvjbhk','uhuyughjko[p[hj'],
]


@bot.message_handler(commands=['start', 'riddle'])
def send_riddle(message):
    riddle = mythology_riddles
    bot.send_message(message.chat.id, riddle[0]["question"])


@bot.message_handler(content_types=['text'])
def check_answer(message):
    if message.text.lower() == mythology_riddles[0]["answer"].lower():
        bot.send_message(message.chat.id, "Correct! Here is more information: " + 'э')
        return 
 
    if message.text in mythology_riddles[1]:
        bot.send_message(message.chat.id, "Correct! " + 'https://en.wikipedia.org/wiki/Cerberus')
        return
            
    else:
        bot.send_message(message.chat.id, "Incorrect, please try again.")


# @bot.message_handler(content_types=['text'])
# def secret(message):

#     for secret in secret_invate: 
#         print(secret)
#         if message == secret:
#             bot.send_message(message.chat.id, "Correct! " + 'https://en.wikipedia.org/wiki/Cerberus')
#             return
#     bot.send_message(message.chat.id, "Incorrect, please try again.")

bot.polling()


