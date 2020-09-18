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

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    await bot.change_presence(activity=discord.Game(name="Ich bin Enigma"))

to = "NzU0NzA4NjUyNzA2"
ke = "NzU4NzI4.X14rNA.SyDYn8-"
n = "P5bHsWb_kYyDvh5QVtcQ"

import help
import wikiarama
import pomodoro
import wikipedia

@bot.command()
async def wiki(ctx,*,words):
    await wikiarama.wikipediarama(ctx, words)

@bot.command(aliases=['neredeyim'])
async def yardım(ctx):
    await help.yardımkomut(ctx)
    
@bot.command()
@commands.has_permissions(kick_members =True)
async def sunucudanat(ctx,member : discord.Member, *, reason="Herhangi bir nedeni yok."):
    await help.at(ctx,member,reason="Herhangi bir nedeni yok.")

@bot.command()
@commands.has_permissions(ban_members = True)
async def banla(ctx,member : discord.Member, *, reason="Herhangi bir nedeni yok"):
    await help.ban(ctx,member,reason="Herhangi bir nedeni yok")

@bot.command()
async def p(ctx,iss,seconds,member : discord.Member):
    await pomodoro.zamanlama(ctx,iss,seconds,member)

@bot.command()
async def pt(ctx, member : discord.Member):
    await pomodoro.zamanlama2(ctx,member)

bot.run(to+ke+n)
