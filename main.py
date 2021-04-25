
import asyncio
from WebSocketClient import WebSocketClient

if __name__ == '__main__':
    # Instancia o cliente do Websocket
    client = WebSocketClient()
    loop = asyncio.get_event_loop()

    # Inicializa a conexação e obtém o protocolo de conexão do cliente
    connection = loop.run_until_complete(client.connect())

    # Inicializa o listener e heartbeat (ping-pong)
    tasks = [
        asyncio.ensure_future(client.heartbeat(connection)),
        asyncio.ensure_future(client.receiveMessage(connection)),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
