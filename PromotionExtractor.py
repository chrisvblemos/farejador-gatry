import requests
from bs4 import BeautifulSoup
import logging

# Extrai a promoção mais recente do site Gatry


class PromotionExtractor():
    def __init__(self):
        self.url = 'http://www.gatry.com'

        self.logger = logging.getLogger('extractor_app')
        self.logger.setLevel(logging.DEBUG)

        self.fh = logging.FileHandler('extractor_app.log')
        self.fh.setLevel(logging.ERROR)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)

        self.fmt = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ch.setFormatter(self.fmt)
        self.fh.setFormatter(self.fmt)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    # Coleta a nova promoção e trata os dados em um Dict
    # Retorna um dict com informações da promoção extraída
    def Get(self):
        promo = {}
        response = requests.get(self.url)
        content = BeautifulSoup(response.content, 'html.parser')
        promotion = content.find('article', 'promocao first')

        promo['name'] = promotion.find(
            'h3', itemprop='name').find('a').getText()
        promo['link'] = promotion.find(
            'h3', itemprop='name').find('a', href=True)['href']
        promo['gatry_link'] = self.url + \
            promotion.find('a', 'mais hidden-xs', href=True)['href']
        promo['price'] = promotion.find(
            'p', 'preco margin-comentario').find('span', itemprop='price').getText()
        promo['user_name'] = promotion.find('p', 'usuario').find('img')[
            'title']
        promo['user_profile'] = self.url + \
            promotion.find('p', 'usuario').find('a', href=True)['href']

        self.logger.info('Found new promotion: {}'.format(promo))
        return promo
