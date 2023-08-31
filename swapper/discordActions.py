import os
import discord
#import pronounSwapper.swapper.pronounSwapper
import asyncio
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('~/Hackerrank/Python/Exercises/pronounSwapper/.env')
load_dotenv()
fart = os.environ['TOKEN']
print(fart)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(fart)