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
description = '''Fcking Pro-ed Nouns.'''
#bot = commands.Bot(command_prefix='?', description=description, intents=intents)

'''@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')'''

'''@bot.command()
async def navy_seal(ctx, message: discord.message):
    if message.author == client.user:
        return

    if message.content.startswith('$navy'):
        await message.channel.send("What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.")

@bot.command()
async def replace(ctx, input: str):
    """Replaces one specified pronoun with another in a message. Input must be \$replace \"old pronoun\" \"new pronoun\" \"message content\""""
    try:
        oldnoun, newnoun, message = map(str, input.split(' ', 2))
    except Exception:
        await ctx.send('pwease format in the following way: \"old pronoun\" \"new pronoun\" \"message content\"')
        return

    result = pronounSwapper.processMessage(oldnoun, newnoun, message)
    await ctx.send(result)

bot.run(fart)'''

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