import telebot
import json, requests

url = 'https://api.foursquare.com/v2/venues/explore'

lati = '-23.204216'
longi = '-45.908808'

bot = telebot.TeleBot('653930137:AAETtiwYIe7nUZ772WK56cNe1zGJOTlcen0')
   
params = dict(
client_id='QP0T1GR444LEPLN1PRRFO3RB3JUWONNFDACBQANVFISXELAR',
client_secret='GGAN2YWTDUQGDZJZG3UJF1LXJGETF5AEICBOAYNSWG4DKAPG',
v='20180323',
ll= ' {}, {}'.format(lati, longi),
query='restaurants',
limit=5)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

n = []
e = []
c = []

for abc in data['response']['groups']:
    for cba in abc['items']:
        try:
            nome = (cba['venue']['name'])
            endereco = (cba['venue']['location']['address'])
            cidade = (cba['venue']['location']['city'])
            lati = (cba['venue']['location']['lat'])
            longi = (cba['venue']['location']['long'])
        except Exception:
            pass
        n.append(nome)
        e.append(endereco)
        c.append(cidade)
    

@bot.message_handler(commands=['start'])
def inicio(mensagem):
    banner = "Olá! Bateu uma fome? Então ativa sua localização que eu te indico o restaurante mais próximo de você!"
    chatid = mensagem.chat.id # type: 18181818181818 -191919191919
    bot.send_message(chatid, banner)

@bot.message_handler(content_types=['location'])
def indica(mensagem):
    lati = mensagem.location.latitude
    longi = mensagem.location.longitude
    chatid = mensagem.chat.id
    banner = 'Segue as melhores opções de restaurante pra você: '
    bot.send_message(chatid, banner)
    i = 0
    while i<len(n):
        banner2 = 'Nome: {} \nEndereco: {} Cidade: {}\n'.format(n[i], e[i], c[i])
        chatid = mensagem.chat.id
        bot.send_message(chatid, banner2)
        bot.send_location(chatid, lati, longi)
        i = i + 1
        
bot.polling()
