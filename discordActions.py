import os
import discord
import swapper.pronounSwapper
import asyncio
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
discord_client = discord.Client()
@discord_client.event
async def on_ready():
    print(f'{discord_client.user} Welcome to  Discord!')
discord_client.run(TOKEN)