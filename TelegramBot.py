import telebot

from settings import TOKEN, CHANNEL

# Definição do Bot do Telegram, insira o TOKEN do seu bot e o canal CHANNEL onde quer enviar as mensagens no arquivo settings.py


class TelegramBot():
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

    def Push(self, promo):
        caption = '<b>🚨🚨🚨 NOVA PROMOÇÃO CHEGANDO, AU AU!\n\n<a href="{}">{}</a>\n💸Preço: R${}</b>\n\n\n💬<a href="{}">Discuta no Gatry!</a>'.format(
            promo['link'], promo['name'], promo['price'], promo['gatry_link'])
        self.bot.send_message(CHANNEL, caption)
