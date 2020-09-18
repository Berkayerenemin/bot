import discord
import os
import random
import discord
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    await bot.change_presence(activity=discord.Game(name="Ich bin Enigma"))


to = "NzU0NzA4NjUyNzA2"
ke = "NzU4NzI4.X14rNA.SyDYn8-"
n = "P5bHsWb_kYyDvh5QVtcQ"

import wiki
import turkdil
import help

@bot.event
async def on_message(message):  
    
    if message.author == bot.user: 
        return

    mesaj = message.content.lower()

    if "!w" in mesaj:
        await wiki.resarch(mesaj, message)
    if "!tdk" in mesaj:
        await turkdil.tdkara(mesaj, message)
    if "!help" == mesaj:
        await help.yardim()
    if "!yardım" == mesaj:
        await help.yardim()

bot.run(to+ke+n)
