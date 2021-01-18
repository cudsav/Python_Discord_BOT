import os

import asyncio

try:

  import discord
  
  from discord.ext import commands
  
except:

  os.system("pip3 install discord.py")
  
bot = commands.Bot(command_prefix = "")

token = "" # Your Discord BOT token string

@bot.event

async def on_ready():

  print("BOT is online now.")
  
@bot.event

async def on_message(message):

  if message.author.id == bot.user.id:
    return
    
  else:
  
    if message.content == "ping":
    
      await message.channel.send("Pong")

bot.run(token)
