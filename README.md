![alt text](https://i.imgur.com/jvJ44cn.png)
# Farejador do Gatry


Um cliente de Websocket que se conecta ao servidor de ws do site Gatry. Quando detecta uma nova promoção, faz uma extração dos dados da promoção e então publica em um canal do Telegram via um bot.

A aplicação está disponível em uma imagem do Docker. Lembre-se de setar o Token do seu Bot e o canal onde deseja que o mesmo publique as mensagens.

# Variáveis de Ambiente

Para a execução correta da aplicação, é necessário que as seguintes variáveis de ambiente estejam configuradas:

- TELEGRAM_BOT_TOKEN
    - Token do seu bot criado no Telegram.
    - [Para criar um bot no telegram, basta seguir esse guia.](https://core.telegram.org/bots)
- TELEGRAM_CHANNEL
    - Canal do Telegram onde o Bot publicará as novas promoções. 
    - O Bot deve estar adicionado ao canal como administrador. 
    - O nome do canal deve ser escrito no formato @nome_do_canal.

# Execução Local

Para executar a aplicação, basta executar o seguinte comando:

`python main.py`
# Docker Build

Basta executar o seguinte comando:

`docker build . -t=gatry-bot`

# Docker Run

Basta executar o seguinte comando:

`docker run --rm -it -e TELEGRAM_BOT_TOKEN=SEU_TOKEN -e TELEGRAM_CHANNEL=CANAL_DO_TELEGRAM gatry-bot`

# Acknowledgements

- 🐕 [Marisa Helena](https://github.com/Isahelena)
    - Organização do código;
    - Logging;
    - Docker Build.