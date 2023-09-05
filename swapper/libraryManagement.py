from typing import List, Optional
import logging
import logging.handlers
from pathlib import Path
from aiohttp import ClientSession
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from aiohttp import ClientSession
import os
import pronounSwapper as swapcommands
import classAttempt as proClass

dotenv_path = Path('~/Hackerrank/Python/Exercises/pronounSwapper/.env')
load_dotenv()
token = os.environ['TOKEN']



class roleLibraryBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents, testing_guild_id: Optional[int] = None) -> None:
        super().__init__(intents=intents, command_prefix='?', description="Keeps track of default + added pronouns for your server.")
        self.Library = {"🟥": ["they", "them", "their", "theirs", "theirself"], "🟧": ["she", "her", "her", "hers", "herself"], 
                      "🟨": ["he", "him", "his", "his", "himself"], "🟩": ["ze", "hir", "hir", "hirs", "hirself"]}
        self.description = ""
        self.channel = ""
        self.role_message_id =""
        self.emoji_to_role = {}
        self.roleID = 0
        #self.web_client = web_client
        self.testing_guild_id = testing_guild_id
        for emoji in self.Library.keys():
            self.emoji_to_role[discord.PartialEmoji(name=emoji)]= self.roleID
            self.roleID+=1



    '''async def setup_hook(self) -> None:
        # This copies the global commands over to your guild.
        #for extension in self.initial_extensions:
            #await self.load_extension(extension)
        if  bot.testing_guild_id:
            testguild = bot.get_guild(int(bot.testing_guild_id))
            # We'll copy in the global commands to test with:
            self.tree.copy_global_to(guild=testguild)
            # followed by syncing to the testing guild.
            await self.tree.sync(guild=testguild)'''

        
        
        

#command_prefix='?', description="Keeps track of default + added pronouns for your server.",

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds =True
intents.guild_messages = True
test_server_id = int(os.environ['SERVER_ID'])
discord.Permissions(permissions=268512368)
bot = roleLibraryBot(intents=intents, testing_guild_id=test_server_id)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id}) (Guild: {bot.guilds})')
    print('------')
    testguild = bot.get_guild(bot.testing_guild_id)
    channel = discord.utils.get(testguild.text_channels, name='roles')
    if channel == None:
        channel = await testguild.create_text_channel(name="roles")
    roleMessageText = swapcommands.makePronounMessage(bot.Library)
    roleMessage = await channel.send(roleMessageText)
    bot.role_message_id = roleMessage.id
    '''if not bot.testing_guild_id:
        listOfServers = bot.guilds
        for server in listOfServers:
            channel = discord.utils.get(server.text_channels, name='Roles')
        if not channel:
            channel = await server.create_text_channel("Roles")
    else:
        testguild = bot.get_guild(bot.testing_guild_id)
        channel = discord.utils.get(testguild.text_channels, name='Roles')
        if not channel:
            channel = await testguild.create_text_channel("Roles")'''
    
'''@bot.command(name="setup")
async def setup(ctx):
    print("i'm here!")
    testguild = bot.get_guild(bot.testing_guild_id)
    channel = discord.utils.get(testguild.text_channels, name='roles')
    if channel == None:
        channel = await testguild.create_text_channel(name="roles")
    roleMessageText = swapcommands.makePronounMessage(bot.Library)
    roleMessage = await channel.send(roleMessageText)
    bot.role_message_id = roleMessage.id'''
    


@bot.command(name="add")
async def add(ctx, subjective: str, objective: str, possessive: str, posspronoun: str, reflexive: str, emoji: str):
    """Adds pronoun set to library. Set must be listed in the following order;
    Subjective (ex. they),
    Objective (ex. them)
    Possessive (ex. their)
    Posessive Pronoun (ex. theirs)
    Reflexive (ex. theirself)
    Emoji to represent pronoun set"""
    testguild = bot.get_guild(bot.testing_guild_id)
    channel = discord.utils.get(testguild.text_channels, name='roles')
    newnouns = [subjective, objective, possessive, posspronoun, reflexive]     
    result = swapcommands.addPronounSet(newnouns, emoji, bot.Library)
    if result == emoji:
        #add modal here so that users know the emoji is already taken.
        pass
    elif result == None:
        #add modal here so that users know that the set is already in the library.
        pass
    else:
        updatedRoleMessage = swapcommands.makePronounMessage(bot.Library)
        rolesMessageForUpdate = await channel.fetch_message(bot.role_message_id)
        await rolesMessageForUpdate.edit(content = "React to this message to gain pronoun role(s).\nFor emoji pronouns, surround pronouns with a mix of text and emoji in quotes.\n"+updatedRoleMessage)
        bot.emoji_to_role[discord.PartialEmoji(name=emoji)]= bot.roleID
        bot.roleID+=1

'''async def main():

    # When taking over how the bot process is run, you become responsible for a few additional things.

    # 1. logging

    # for this example, we're going to set up a rotating file logger.
    # for more info on setting up logging,
    # see https://discordpy.readthedocs.io/en/latest/logging.html and https://docs.python.org/3/howto/logging.html

    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Alternatively, you could use:
    # discord.utils.setup_logging(handler=handler, root=False)

    # One of the reasons to take over more of the process though
    # is to ensure use with other libraries or tools which also require their own cleanup.

    # Here we have a web client and a database pool, both of which do cleanup at exit.
    # We also have our bot, which depends on both of these.
    #clientToFindGuild = discord.client(intents=intents)

    #async with ClientSession() as our_client:
        # 2. We become responsible for starting the bot.
        #guild = clientToFindGuild.get_guild(id=roleLibraryBot.setup_hook.guildid)

        #exts = ['general', 'mod', 'dice']
    async with roleLibraryBot(intents=intents) as bot:
        await bot.start(token)
        


# For most use cases, after defining what needs to run, we can just tell asyncio to run it:
asyncio.run(main())'''
'''async def main():
    await bot.start(token)

asyncio.run(main())'''

bot.run(token)