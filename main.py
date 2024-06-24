import discord
import random
from discord.ext import commands
import secret

# Configurações do bot
TOKEN = secret.Token()
INTENTS = discord.Intents.default()
INTENTS.reactions = True
INTENTS.guilds = True
INTENTS.members = True

bot = commands.Bot(command_prefix='/', intents=INTENTS)

# IDs dos cargos
ROLES = [
    1233585397674807306,  # Transportador
    1233585496182100060,  # Lixeiro
    1233585570224279562,  # Filtrador
    1233585639337885696,  # Clasificador
    1233585729968541788,  # Aplicador
    1233585794543779901,  # Analista
]

# IDs dos emojis
ASSIGN_ROLE_EMOJI = '🎲'  # Emoji para atribuir cargos
REMOVE_ROLE_EMOJI = '❌'  # Emoji para remover cargos

# Mensagem de referência para as reações (substitua pelo ID real da mensagem)
MESSAGE_ID = 1251707323508854845

assigned_roles = set()

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != MESSAGE_ID:
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if member.bot:
        return

    emoji = payload.emoji.name  # Obtém o nome do emoji reagido

    if emoji == ASSIGN_ROLE_EMOJI:
        await assign_role(member)
    elif emoji == REMOVE_ROLE_EMOJI:
        await remove_roles(member)

async def assign_role(member):
    guild = member.guild
    available_roles = [guild.get_role(role_id) for role_id in ROLES if role_id not in assigned_roles]

    if not available_roles:
        await member.send("Todos os cargos já foram atribuídos.")
        return

    selected_role = random.choice(available_roles)
    await member.add_roles(selected_role)
    assigned_roles.add(selected_role.id)

    await member.send(f"Cargo {selected_role.name} atribuído com sucesso!")

async def remove_roles(member):
    guild = member.guild
    roles_to_remove = [guild.get_role(role_id) for role_id in ROLES if guild.get_role(role_id) in member.roles]

    for role in roles_to_remove:
        await member.remove_roles(role)
        if role.id in assigned_roles:
            assigned_roles.remove(role.id)

    await member.send("Todos os cargos foram removidos!")

# ID do canal de voz fixo
VOICE_CHANNEL_ID = 1254611602792251404

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and after.channel.id == VOICE_CHANNEL_ID:
        # Verificar o número de membros no canal de voz
        members_in_channel = len(after.channel.members)

        if members_in_channel == 6:
            await assign_impostor_and_supervisor(after.channel.members)

async def assign_impostor_and_supervisor(members):
    # Garantir que os membros selecionados sejam diferentes entre si
    impostor, supervisor = random.sample(members, 2)
    
    # Enviar mensagem apenas para impostor
    try:
        await impostor.send("Você é o impostor (Destrua a fábrica).")
    except discord.Forbidden:
        print("Não foi possível enviar mensagem para o impostor.")

    # Enviar mensagem apenas para supervisor
    try:
        await supervisor.send("Você é o supervisor (Descubra quem é o impostor).")
    except discord.Forbidden:
        print("Não foi possível enviar mensagem para o supervisor.")

bot.run(TOKEN)