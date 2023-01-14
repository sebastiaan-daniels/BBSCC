# package imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

# load env
load_dotenv("..\\util\\.env")

# connect to client and bot
intents = discord.Intents.default()
bot = commands.Bot(debug_guilds=[int(getenv('debug_guild'))] if getenv('bot_type') == 'dev' else None, intents=intents, help_command=None)

# import logging
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

# adding the cogs
cogs_list = [
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

# get bot token and run bot
token = getenv('BOT_TOKEN')
bot.run(token)