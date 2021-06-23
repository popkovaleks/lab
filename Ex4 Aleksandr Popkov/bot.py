import telebot
import requests
import time
from flask import jsonify

TOKEN = "*"

bot = telebot.TeleBot(TOKEN, threaded=False)

HEALTH = 'http://localhost:5000/health'
QUESTION = 'http://localhost:5000/question'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	
    response = requests.get(HEALTH)

    if (response.json()['status'] == "OK"):
        
        
        print(message)
        
        question_to_send = {'question': message.text}
        print(question_to_send)
        r_post = requests.post(QUESTION, json=question_to_send)
        print('_____')
        print(r_post.json())
        response = r_post.json()
        answer = """{}\nNamed entities: {}\nRelation: {}""".format(response['answer_text'], response['named_entities'], response['relation'][0])
        bot.reply_to(message, answer)


while True:
    try:
        bot.polling()
    
    except Exception as e:
        print(e)
        time.sleep(15)