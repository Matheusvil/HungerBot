import telebot
import json, requests

url = 'https://api.foursquare.com/v2/venues/explore'

bot = telebot.TeleBot('653930137:AAETtiwYIe7nUZ772WK56cNe1zGJOTlcen0')

params = dict(
  client_id='QP0T1GR444LEPLN1PRRFO3RB3JUWONNFDACBQANVFISXELAR',
  client_secret='GGAN2YWTDUQGDZJZG3UJF1LXJGETF5AEICBOAYNSWG4DKAPG',
  v='20180323',
  ll='-23.215064, -45.887075',
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

@bot.message_handler(commands=['start'])
def inicio(mensagem):
    banner = "Olá! Bateu uma fome? Então manda sua localização que eu te indico o restaurante mais próximo de você!"

    chatid = mensagem.chat.id # type: 18181818181818 -191919191919
    bot.send_message(chatid, banner)

@bot.message_handler(commands=['localizacao'])
def indica(mensagem):
    banner = 'Nome: {} \nEndereco: {} Cidade: {}'.format(nome, endereco, cidade)

    chatid = mensagem.chat.id
    bot.send_message(chatid, banner)

@bot.message_handler(commands=['ajuda'])
def indica(mensagem):
    banner = 'Não se preocupa, vou responder suas dúvidas!\n\nO Hunger Bot funcionar da seguinte maneira:\n- Primeiro você envia sua localização\n-Depois você envia o comando /localizacao e a gente informa o restaurante pra você ;)\n\nSe você não está conseguindo mandar sua localização, verifica se ela está ativa.'

    chatid = mensagem.chat.id
    bot.send_message(chatid, banner)

bot.polling()
