import websockets
import asyncio
import logging

from Consumer import Consumer

# Cliente websocket responsável por ser conectar ao websocket da Gatry


class WebSocketClient():
    def __init__(self):
        self.logger = logging.getLogger('websocket_client')
        self.logger.setLevel(logging.DEBUG)

        self.fh = logging.FileHandler('websocket_client.log')
        self.fh.setLevel(logging.ERROR)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)

        self.fmt = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ch.setFormatter(self.fmt)
        self.fh.setFormatter(self.fmt)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    # Inicializa a conexão
    async def connect(self):
        self.consumer = Consumer()
        self.connection = await websockets.client.connect('wss://ws-mt1.pusher.com/app/a350d71befcecdb171ea?protocol=7&client=js&version=7.0.3&flash=false')
        if self.connection.open:
            self.logger.info(
                'Conexão com websocket estabelecida... Cliente conectado com sucesso!')
            # Inscreve-se no canal gatry-site para receber notificações de promoções novas
            await self.sendMessage('{"event":"pusher:subscribe","data":{"auth":"","channel":"gatry-site"}}')
            return self.connection

    # Envia uma mensagem
    async def sendMessage(self, message):
        await self.connection.send(message)

    # Recebe nova mensagem
    async def receiveMessage(self):
        while True:
            try:
                message = await self.connection.recv()
                self.logger.info(
                    'Nova mensagem recebida do servidor: {}'.format(message))

                # O consumidor executa sempre que uma nova mensagem chega (ver Consumer.py)
                self.consumer.proccess(message)
            except websockets.exceptions.ConnectionClosed:
                self.logger.error('Conexão com servidor perdida!')
                self.logger.info('Tentando reestabelecer conexão...')
                await self.connect()
                await asyncio.sleep(5)

    # Envia uma mensagem de ping para o servidor ws da Gatry a cada 120 segundos
    async def heartbeat(self):
        while True:
            try:
                self.logger.info('Pingando o servidor...')
                await self.connection.send('{"event":"pusher:ping","data":{}}')
                await asyncio.sleep(120)
            except websockets.exceptions.ConnectionClosed:
                self.logger.error('Conexão com servidor perdida!')
                self.logger.info('Tentando reestabelecer conexão...')
                await self.connect()
                await asyncio.sleep(5)
