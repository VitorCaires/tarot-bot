import discord
from discord.ext import commands
import json
import random
import scrap

#definindo o prefixo das chamada de comando e as permissões
client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

#transformando o arquivo json em uma lista com todos os arcanos maiores
archive = open("tarot.json")
tarotlist = json.load(archive)

#conectando o bot
@client.event
async def on_ready():
    print('tudo certo')
    print('-----------')

#evita que o bot chame a si mesmo
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

#envia uma carta aleatória para o solicitante, com tempo de espera de um dia
@client.command(pass_context = True)
@commands.cooldown(1,60*60*24, commands.BucketType.user)
async def dtarot(ctx):
    n = str(random.randint(0,21))
    embed = discord.Embed(title = tarotlist[n]["title"], description = tarotlist[n]["description"], color = discord.Color.from_str(tarotlist[n]["color"]))
    embed.set_thumbnail(url = tarotlist[n]["image_url"])
    await ctx.channel.send(embed = embed)
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.channel.send(embed = embed)

#envia o horóscopo diário chamando um script que faz o scraping do site: https://f5.folha.uol.com.br/horoscopo/
@client.command()
async def horoscopo(ctx, signo):
    signo = signo
    msg = scrap.daily[signo]
    await ctx.channel.send(msg)

client.run('TOKEN DO BOT AQUI')
