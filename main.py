import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='_')

@bot.event
async def on_ready():
    print('Ready')


@bot.command()
async def echo(ctx, *, content):
    await ctx.send(content)

bot.run(os.environ['BOT_TOKEN'])
