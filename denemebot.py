import discord
import os
import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import errors
import wiki2
import time as t
import yenidenp
import yardim
import yenis

#Bot prefix
bot = commands.Bot(command_prefix='!')

#Açılış
@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    print(f'{bot.user.id} sunucuda...')
    await bot.change_presence(activity=discord.Game(name="Hazırlanıyor: Versiyon 0.9"))

#Yeni üye
@bot.event
async def on_member_join(member):
    await member.create_dm()

#Olaylar
@bot.event
async def on_message(ctx):
    global yazi
    if ctx.author == bot.user:
        return
    mesaj = ctx.content.lower()
    msj= mesaj.split()
    print(msj)

    if msj[0] == '!w':
        yazi = await ctx.channel.send("Bir şeyler")

    if msj[0] == '!s':
        await yazi.edit(content="Başka bir şeyler")
    else:
        pass
bot.run("NzU0NzA4NjUyNzA2NzU4NzI4.X14rNA.ZeX9XHQklezSQ7UvDd5egBAl61c")