import telebot
import json, requests
import time

url = 'https://api.foursquare.com/v2/venues/explore'

bot_token = '653930137:AAETtiwYIe7nUZ772WK56cNe1zGJOTlcen0'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['iniciar'])
def send_iniciar(message):
    bot.reply_to(message, 'Ola, seja bem vindo ao HungerBot!')

@bot.message_handler(commands=['ajuda'])
def send_ajuda(message):
    bot.reply_to(message, 'utilize /localização para encontrar o restaurante mais próximo!')

@bot.message_handler(commands=['localizacao'])
def send_localizacao(message):
    bot.reply_to(message, 'Esses são os restaurantes mais proximos de você:',+descobre_localizacao(nome, endereco))    

def descobre_localizacao(nome, endereco): 
    params = dict(
      client_id='QP0T1GR444LEPLN1PRRFO3RB3JUWONNFDACBQANVFISXELAR',
      client_secret='GGAN2YWTDUQGDZJZG3UJF1LXJGETF5AEICBOAYNSWG4DKAPG',
      v='20180323',
     ll='-23.161942,-45.795344',
      query='restaurants',
     limit=1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    for abc in data['response']['groups']:
        for cba in abc['items']:
            try:
                nome = (cba['venue']['name'])
                endereco = (cba['venue']['location']['address'])
                cidade = (cba['venue']['location']['city'])
            except Exception:
                pass
            
    return nome, endereco

while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(1.5)
