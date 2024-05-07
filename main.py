import discord
import random
import asyncio
from secret import Token

# Token do seu bot Discord
TOKEN = Token()

# Lista de IDs dos canais onde os jogadores enviarão mensagens
canais_jogadores = [
    1000000000000001, 
    1000000000000002,
    1000000000000003,
    1000000000000004,
    1000000000000005,
    1000000000000006
]

# Funções dos jogadores
funcoes = ['Transportador', 'Lixeiro', 'Filtrador', 'Classificador', 'Aplicador', 'Analista']

# Inicialização do cliente Discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# Lista para armazenar os textos dos jogadores
textos_jogadores = []

@client.event
async def on_ready():
    print('Bot está online!')

@client.event
async def on_message(message):
    if message.content.startswith('/start'):
        await message.channel.send('Para jogar, reaja a esta mensagem com o emoji 🎲.')

@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    # Checa se a reação é a desejada e conta quantas reações foram recebidas
    if str(reaction.emoji) == '🎲':
        if len(reaction.message.reactions) >= 6:
            await iniciar_jogo()

async def iniciar_jogo():
    # Limpa a lista de textos dos jogadores
    textos_jogadores.clear()

    # Aguarda 120 segundos para os jogadores enviarem seus textos
    await asyncio.sleep(120)

# Coleta a última mensagem de cada canal dos jogadores
for canal_id in canais_jogadores:
    canal = client.get_channel(canal_id)
    messages = await canal.history(limit=1).flatten()
    if messages:
        textos_jogadores.append(messages[0].content)

# Conecta ao servidor do Discord
client.run(TOKEN)