# Import some necessary modules for this BOT.
import asyncio
import json
import requests # "pip3 install requests"
import discord # "pip3 install discord"
from discord.ext import commands
bot = commands.Bot(command_prefix = "")
DISCORD_BOT_TOKEN = "YOUR DISCORD TOKEN HERE"
@bot.event
async def on_ready():
    print("BOT is online")
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    else:
        if message.content.startswith("!delete"): # You must set role as a admin for your BOT
            await message.channel.purge(limit = int(message.content[8:]))
        else:
            req = requests.get(f"https://api.simsimi.net/v1/?text={message.content}") # You can add &lang=... to set your BOT's languages
            res = json.loads(req.text)
            await message.channel.send(res["messages"][0]["response"])
bot.run(DISCORD_BOT_TOKEN)
