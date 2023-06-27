import discord
from discord.ext import commands
import sys, traceback
import os

token = Njk3MTUwODYzNzk3Mzg3MzA0.GhZrUp.2Eu3uqdZKx1sJTTqHeU5qVKiw1m5DHMFjtAZRg

prefix = '!'

bot = commands.Bot(command_prefix=prefix, description='R6 Stats Bot')
bot.remove_command('help')

extensions = ['commands']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'Ready as: {bot.user.name}')
    game = discord.Game("Rainbow Six Siege")
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run(token, bot=True, reconnect=True) 
