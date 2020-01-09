from random import Random
from time import sleep
import requests
import telebot
from lxml.html import fromstring

user_agent = [0] * 7478
bot = telebot.TeleBot('995833439:AAFYs05f5kc1fvrH86q_X1shVFMUmv31E9k')


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот запущен, введите интересующий URL для создания запросов')


@bot.message_handler(content_types=['text'])
def send_text(message):

    with open('user-agents.txt', 'r') as users:
        for cnt, line in enumerate(users):
            user_agent[cnt] = {'User-agent': line[:-1]}

    url_from_bot = message.text
    count = 10
    while count >= 0:
        rand_int = Random().randint(0, 7478)
        # rand_proxy = Random().randint(0, len(get_proxies()))
        rand_proxy = get_proxies()
        print(rand_proxy)
        resp = requests.get('https://' + url_from_bot, headers=user_agent[rand_int])
        print(resp)
        count -= 1
        sleep(1)
        if count == 0:
            bot.send_message(message.chat.id, 'Запрос успешно обработан')


bot.polling()



