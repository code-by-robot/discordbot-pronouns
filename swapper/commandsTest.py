from typing import Optional
from pathlib import Path
import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import pronounSwapper as swapcommands

dotenv_path = Path('~/Hackerrank/Python/Exercises/pronounSwapper/.env')
load_dotenv()
fart = os.environ['TOKEN']
server_id = os.environ['SERVER_ID']

MY_GUILD = discord.Object(id=server_id)  # replace with your guild id


'''class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.role_message_id = 0  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 0,  # ID of the role associated with unicode emoji '🔴'.
            discord.PartialEmoji(name='🟡'): 0,  # ID of the role associated with unicode emoji '🟡'.
            discord.PartialEmoji(name='green', id=0): 0,  # ID of the role associated with a partial emoji's ID.
        }

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


@client.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')


# The rename decorator allows us to change the display of the parameter on Discord.
# In this example, even though we use `text_to_send` in the code, the client will use `text` instead.
# Note that other decorators will still refer to it as `text_to_send` in the code.
@client.tree.command()
@app_commands.rename(text_to_send='text')
@app_commands.describe(
    oldnoun ='Original pronoun in message.',
    newnoun = 'Pronoun you want to be used in new message.',
    text_to_send='Message that you want the pronouns to be replaced in.'
)
async def replace(interaction: discord.Interaction, oldnoun: str, newnoun: str, text_to_send: str):
    """Sends the text into the current channel."""
    try:
        _command, oldnoun, newnoun, newMessage = map(str, message.content.split(' ', 3))
        await message.delete()
    except Exception:
        await message.channel.send('pwease format in the following way: \"old pronoun\" \"new pronoun\" \"message content\"')
        return
            
    result = swapcommands.processMessage(oldnoun, newnoun, text_to_send)

    await interaction.response.send_message(result)


# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.
@client.tree.command()
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def assign(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    """Says when a member joined."""
    # If no member is explicitly provided then we use the command user here
    member = member or interaction.user

    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

client.run(fart)'''