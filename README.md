# BixosBot
Bot feito para pingar todos os bixos e as bixetes de 2020 do setor de TI do DASI

Construído baseado nos links:

https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6
https://github.com/Kerooker/PlayCSTelegramBot

Link útil para quem optar por hospedar o bot no GCloud: https://medium.com/@xabaras/setting-your-telegram-bot-webhook-the-easy-way-c7577b2d6f72

Basicamente, o arquivo *main.py* presente nesse repositório é onde está localizada a função principal do bot e o arquivo *requeriments.txt* é onde estão
listadas todas as dependências que precisam ser instaladas localmente na sua máquina para que o bot funcione (o primeiro link também ensina como gerar ele)https://medium.com/@xabaras/setting-your-telegram-bot-webhook-the-easy-way-c7577b2d6f72.
Vale lembrar que as variáveis que possuem um conteúdo sensível, como a 'USERS_TO_PING', que contém todos os users dos bixos e 
bixetes e a 'TELEGRAM_TOKEN', que contém o token do bot, *nunca* devem ser colocadas diretamente no código, pois qualquer pessoa
poderá ver e potencialmente fazer mal uso das mesmas. Elas devem ser postas em um arquivo fora do repositório ou, no caso da hospedagem
feita no GCloud, nas variáveis de ambiente do projeto que você criou.

Outro ponto importante para a construção do bot é que você precisa primeiro criá-lo no seu telegram através do BotFather (vido primeiro link acima).

Depois de construído o algoritmo, é necessário ainda hospedá-lo em algum serviço na nuvem para que ele esteja sempre funcionando.
Por uma questão de padronização, o DASI hospeda todos os seus bots do Telegram pelo Google Cloud ou pelo Heroku. Você pode ver mais sobre isso
e saber como configurar e dar os primeiros passos nessas plataformas [aqui](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots).

Por fim, depois de contruído e hospedado, só resta testá-lo no telegram e ver se está tudo funcionando conforme o esperado.
