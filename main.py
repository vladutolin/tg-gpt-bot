import telebot
import openai
import datetime

token = "YOUR TOKEN"

openai_api_key = 'YOUR KEY'


openai.api_key = (openai_api_key)

def openai_api(message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=1000,
    
    )

    return response['choices'][0]['text']
    

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def qa(message):
    print('Username: ', message.from_user.username, ' Имя: ', message.from_user.first_name, ' Дата: ',datetime.datetime.fromtimestamp(message.date))
    print('Вопрос: ', message.text)
    bot.send_message(message.chat.id, 'Please, wait...')
    bot.send_message(message.chat.id, openai_api(message))

print('start')

try:
    bot.polling(none_stop=True)
except:
    print('WARNING')
