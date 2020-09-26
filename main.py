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

"""@bot.event
async def on_error(ctx, err):
    print(err)
    if err == "CommandNotFound":
        await ctx.channel.send("Bir şeyler yanlış gitti...")"""

@bot.event
async def on_command_error(ctx, exp):
    await ctx.channel.send("Böyle bir komut hafızamda bulunmuyor!")
    print(exp)

"""@bot.event
async def commands.error.CommandNotFound(ctx, exc):
    await ctx.channel.send("Böyle bişi yok.")

@bot.event
async def commands.error.MissingRequiredArgument(ctx, exc):
    await ctx.channel.send("Argüman yok")"""

@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    await bot.change_presence(activity=discord.Game(name="Geliştirme Aşamasında..."))

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

@bot.command(aliases=['neredeyim', 'kayboldum'])
async def yardım(ctx):
    await help.yardımkomut(ctx)
    
"""@bot.command()
@commands.has_permissions(kick_members =True)
async def sunucudanat(ctx,member : discord.Member, *, reason="Herhangi bir nedeni yok."):
    await help.at(ctx,member,reason="Herhangi bir nedeni yok.")

@bot.command()
@commands.has_permissions(ban_members = True)
async def banla(ctx,member : discord.Member, *, reason="Herhangi bir nedeni yok"):
    await help.ban(ctx,member,reason="Herhangi bir nedeni yok")"""

@bot.command(aliases=['pomodoro'])
async def p(ctx,iss,dk):
    k = int(dk)
    seconds = k*60
    await pomodoro.zamanlama(ctx,iss,seconds)

@bot.command()
async def pt(ctx):
    await pomodoro.zamanlama2(ctx)

@bot.command(aliases=['selam',"naber","ooo","heybot"])
async def merhaba(ctx):
    await ctx.channel.send(f"Merhaba {ctx.author.mention}!")
    print(ctx.author.id)
    print(ctx.author.name)

bot.run("NTk0MTk0NDIwMDE5MjMyNzg2.XRY4rQ.jHyat6uWxhnsDJI6MHv4UJkbuB4")
