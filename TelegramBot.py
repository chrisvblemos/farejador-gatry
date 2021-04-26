import telebot
import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL = os.getenv('TELEGRAM_CHANNEL')

# Definição do Bot do Telegram, lembre-se de setar o TOKEN e o canal do Telegram nas variáveis de ambiente, como descrito no README


class TelegramBot():
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

    def Push(self, promo):
        caption = '<b>🚨🚨🚨 NOVA PROMOÇÃO CHEGANDO, AU AU!\n\n<a href="{}">{}</a>\n💸Preço: R${}</b>\n\n\n💬<a href="{}">Discuta no Gatry!</a>'.format(
            promo['link'], promo['name'], promo['price'], promo['gatry_link'])
        self.bot.send_message(CHANNEL, caption)
