import json
import logging

from PromotionExtractor import PromotionExtractor
from TelegramBot import TelegramBot

# O consumer lê e processa mensagens recebidas do websocket do Gatry


class Consumer():
    def __init__(self):
        self.promoExtractor = PromotionExtractor()
        self.telegramBot = TelegramBot()

        self.logger = logging.getLogger('consumer_app')
        self.logger.setLevel(logging.DEBUG)

        self.fh = logging.FileHandler('consumer_app.log')
        self.fh.setLevel(logging.ERROR)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)

        self.fmt = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ch.setFormatter(self.fmt)
        self.fh.setFormatter(self.fmt)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    # Processa uma nova mensagem lida
    def proccess(self, message):

        message = json.loads(message)
        event = message['event']

        # Se um evento chegou e é do tipo new.promotion, loga e então executa a extração e push da mensagem para o canal do Telegram (usando a API de Bots do Telegram)
        if event == 'notification.new.promotion':
            self.logger.info('New promotion(s) proccessed.')
            self.telegramBot.Push(self.promoExtractor.Get())
        else:
            self.logger.debug(
                'New ignored event proccessed. Event: {}'.format(message))
