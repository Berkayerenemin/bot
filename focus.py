import discord
import os
import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import errors
import time as t

token = os.environ.get('BOT-TOKEN')
#Bot prefix
bot = commands.Bot(command_prefix='.')
role_id = 771647376385507339

@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    print(f'{bot.user.id} sunucuda...')
    await bot.change_presence(activity=discord.Game(name="Patrobot Extension"))

@bot.event
async def on_voice_state_update(member, before, after):
    role = discord.utils.get(member.guild.roles, id=role_id)
    if before.channel is None and after.channel is not None:
        #role =discord.utils.get(member.guild.roles, name="focus")
        #await member.add_roles(role)
        #await member.guild.system_channel.send("Alarm!")
        if after.channel.id == 771647652232036352:
            await member.add_roles(role)
            #await member.channel.send("Alarm!")
        else:
            await member.remove_roles(role)

    elif before.channel is not None and after.channel is not None:
        if after.channel.id == 771647652232036352:
            await member.add_roles(role)
            #await member.channel.send("Alarm!")
        else:
            await member.remove_roles(role)

    elif before.channel is not None and after.channel is None:
        if before.channel.id == 771647652232036352:
            await member.remove_roles(role)
        else:
            pass

    else:
        pass

bot.run(token)
