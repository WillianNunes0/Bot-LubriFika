# Importações
import requests
import json
from secret import webhook_key

# URL do webhook do Discord (Oculta por questões de segurança)
webhook_url = webhook_key()

# Dados a serem enviados
data = {
  "content": None,
  "embeds": [
    {
      "title": "LubriFika",
      "description": "||@everyone||",
      "url": "https://github.com/WillianNunes0/Bot-Chapoca",
      "color": 16774400,
      "fields": [
        {
          "name": "Background",
          "value": "Você está em uma fábrica que está passando por dificuldades o gerente liga para o supervisor irritado querendo providências\njá que as ações da empresa estão em queda por conta de um impostor ele o dá uma arma com apenas uma munição e o fala\npara se disfarçar entre os funcionários identifica-lo e neutraliza-lo , o futuro da fábrica depende de você ..."
        },
        {
          "name": "Regras",
          "value": "-> Cada rodada terá a duração de 2 minutos para os jogadores escreverem o seu texto e 30 segundos por texto durante a análise\n\n-> São de função dos integrantes do grupo x perguntarem sobre ...\n\tTransportador -> transporte, armazenamento e manuseio de lubrificantes\n\tLixeiro -> descarte de lubrificantes\n\tFiltrador -> técnicas de filtragem e reciclagem de lubrificantes\n\tClassificador -> classificação dos lubrificantes\n\tAplicador -> métodos de aplicação dos lubrificantes\n\tAnalista -> análise de lubrificantes em uso\n\n-> Com 3 Textos errônios passados a fábrica entrara em colapso e o impostor será vitorioso será possivel ver o estado da fábrica no tabuleiro\n   \n-> O impostor pode tentar adivinhar quem é o supervisor , caso erre ele perderá\n\n-> O supervisor só tem uma chance para encontrar o Impostor \n\n-> Sobre as cartas de Lubirot :\n\tSteve : á discursão só será por emojis\n\tCj : só poderão escrever os textos em inglês \t\n\t..."
        }
      ],
      "image": {
        "url": "https://media4.giphy.com/media/4NpFRswNw7KY2fSTD9/giphy.gif?cid=790b7611f07d427dcce4885e823f6de8ab392bf927828be7&rid=giphy.gif&ct=g"
      },
      "thumbnail": {
        "url": "https://media4.giphy.com/media/rjuQanNOiR7MfRxbOU/200w.gif?cid=6c09b952mst1mvkntit9nilekjljwxwqugg13o2iyvbpzpcu&ep=v1_gifs_search&rid=200w.gif&ct=g"
      }
    }
  ],
  "username": "[Clebin do Honda Civic]",
  "attachments": []
}

# Converter os dados para JSON
json_data = json.dumps(data)

# Enviar a mensagem para o webhook
response = requests.post(webhook_url, data=json_data, headers={'Content-Type': 'application/json'})

# Verificar se a mensagem foi enviada com sucesso
if response.status_code == 200:
    print('Mensagem enviada com sucesso!')
else:
    print('Erro ao enviar mensagem:', response.status_code)
    print(response.text)
    