import discord
from discord.ext import commands
import os
import threading
from web import run_web

INTENTS = discord.Intents.default()
INTENTS.message_content = True 

bot = commands.Bot(command_prefix="$", intents=INTENTS)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def say(ctx, *, mensaje):
    await ctx.send(mensaje)

threading.Thread(target=run_web).start()

bot.run(os.environ["TOKEN"])