# BixosBot
Bot feito para pingar todos os bixos e as bixetes de 2020 do setor de TI do DASI

### Material de apoio para o desenvolvimento:

- O tutorial [desenvolvendo o seu primeiro chatbot no telegram com python](https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6)
- O repositório [PlayCSTelegramBot](https://github.com/Kerooker/PlayCSTelegramBot), que possui funcionalidade semelhante.

### Infraestrutura

Nós optamos por hospedar o bot na Google Cloud, utilizando a `Cloud Functions`. Se você desejar hospedar da mesma maneira, dê uma olhada no guia [_setting-your-telegram-bot-webhook-the-easy-way](https://medium.com/@xabaras/setting-your-telegram-bot-webhook-the-easy-way-c7577b2d6f72)

### Fluxo geral da aplicação

O arquivo [`main.py`](/main.py) contém a função principal do bot, enquanto o arquivo [`requirements.txt`](/requirements.txt) lista as dependências necessárias para executá-lo. No tutorial [desenvolvendo o seu primeiro chatbot no telegram com python](https://medium.com/@mdcg.dev/desenvolvendo-o-seu-primeiro-chatbot-no-telegram-com-python-a9ad787bdf6) citado como material de apoio também é ensinado como montar o `requirements.txt`.

O `main` utiliza variáveis que possuem conteúdo sensível, como a `USERS_TO_PING`, que contém o usuário do Telegram a notificar, ou a `TELEGRAM_TOKEN`, que contém o segredo para utilizar o bot na rede do app. Estas variáveis são mantidas como variáveis de ambiente, e não junto ao código, e **nunca** deve ficar disponível no repositório.

### Criando um Bot

Os bots no Telegram precisam ser criados numa conversa com o bot `@BotFather` no próprio aplicativo. O tutorial de desenvolvimento explica bem a fundo como isso é feito.

Depois de construído o algoritmo, é necessário ainda hospedá-lo em algum serviço na nuvem para que ele esteja sempre funcionando. Nós optamos pela Google Cloud, mas a biblioteca [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot), que utilizamos neste bot explica [Onde hospedar Bots do Telegram](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots).


### Passo-a-passo para a Google Cloud

1- Acesse [o console da google cloud](https://console.cloud.google.com/home/)

2 - Na barra superior, do lado esquerdo da barra de busca selecione o projeto que você irá usar como "link" do seu código com
o bot criado no telegram (Se ele ainda não existe, crie-o)

3 - Depois de aberto, procure na barra esquerda as `Cloud functions` (Ou [acesse-as diretamente](https://console.cloud.google.com/functions/list))

4 - Crie uma se não houver nenhuma

5 - Adicione um anexo.zip ou cole o código do seu arquivo `main.py` e `requeriments.txt`

   5.1 - Vale lembrar que para o bot desse repositório, foi necessária a inclusão apenas da dependência `python-telegram-bot`

6 - Defina a função `webhook` para ser executada na caixa de texto abaixo do editor inline

7 - Defina as variáveis do ambiente no final da página (as variáveis que possuem conteúdo sensível, como o token do seu bot);

8 - Dê um nome para a sua função no início da página

9 - Crie a função

10 - Inicie o seu bot no telegram pesquisando pelo @ dele, clicando na conversa e clicando em `start bot` e teste os comandos implementados pelo seu código
