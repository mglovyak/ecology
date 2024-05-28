import discord, random,os, requests
from discord.ext import commands
from funk import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def facts(ctx):
    await ctx.send(eco_fact())

@bot.command()
async def noecology(ctx):
    await ctx.send(noecology_facts())
    
@bot.command()
async def eco(ctx):
    img=os.listdir('img_eco')
    with open(f'img_eco/{random.choice(img)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run()
