from telebot import TeleBot, types
import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL = os.getenv('TELEGRAM_CHANNEL')

# Definição do Bot do Telegram, lembre-se de setar o TOKEN e o canal do Telegram nas variáveis de ambiente, como descrito no README


class TelegramBot():
    def __init__(self):
        self.bot = TeleBot(TOKEN, parse_mode='HTML')

    def KeyboardFactory(self, url):
        return [
            [
                types.InlineKeyboardButton(
                    "💬 Discuta no Gatry!", url=url),
            ]
        ]

    def Push(self, promo):
        caption = '''<b>🚨 NOVA PROMOÇÃO CHEGANDO, AU AU!

        🔥 <a href="{}">{}</a>
        💸 Preço: R$ {}</b>
        👽 Enviado por: <a href="{}">{}</a>
        '''.format(
            promo['link'], promo['name'], promo['price'], promo['gatry_link'], promo['user_name'], promo['user_profile'])
        reply_markup = types.InlineKeyboardMarkup(
            self.KeyboardFactory(promo['gatry_link']))
        self.bot.send_message(CHANNEL, caption, reply_markup=reply_markup)
