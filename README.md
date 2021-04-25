# Farejador do Gatry

Um cliente de Websocket que se conecta ao servidor de ws do site Gatry. Quando detecta uma nova promoção, faz uma extração dos dados da promoção e então publica em um canal do Telegram via um bot.

A aplicação está disponível em uma imagem do Docker. Lembre-se de setar o Token do seu Bot e o canal onde deseja que o mesmo publique as mensagens.
# Build

Basta executar o seguinte comando:

`docker build . -t=gatry-bot`

# Execução

Basta executar o seguinte comando:

`docker run --rm -it -e TELEGRAM_BOT_TOKEN=SEU_TOKEN -e TELEGRAM_CHANNEL=CANAL_DO_TELEGRAM gatry-bot`