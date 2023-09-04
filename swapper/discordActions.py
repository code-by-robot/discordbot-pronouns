import os
import discord
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from discord.ext import commands
from discord import ui
import pronounSwapper as swapcommands

dotenv_path = Path('~/Hackerrank/Python/Exercises/pronounSwapper/.env')
load_dotenv()
fart = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = discord.Client(intents=intents)
description = '''Pro-ed Nouns.'''
#bot = commands.Bot(command_prefix='?', description=description, intents=intents)

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
       
        elif message.content.startswith('!replace'):
            try:
                _command, oldnoun, newnoun, newMessage = map(str, message.content.split(' ', 3))
                await message.delete()
            except Exception:
                await message.channel.send('pwease format in the following way: \"old pronoun\" \"new pronoun\" \"message content\"')
                return
            
            result = swapcommands.processMessage(oldnoun, newnoun, newMessage)
            await message.channel.send(result)

client = MyClient(intents=intents)
client.run(fart)