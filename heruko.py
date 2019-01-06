import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
Client = commands.Bot(command_prefix = ".")
@Client.event
async def on_ready():
    print("Thanks")
    await client.change_presence(game=discord.Game(name="videos"))

@Client.event
async def on_message(message):
    if message.content.startswith('.hello'):
        msg = 'Hello {0.author.mention} How are you'.format(message)
        await client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))
