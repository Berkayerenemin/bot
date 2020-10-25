#Kütüphaneler
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
import yardim
import pomodoro

token = os.environ.get('BOT-TOKEN')

#Bot prefix
bot = commands.Bot(command_prefix='.')

#Açılış
@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    print(f'{bot.user.id} sunucuda...')
    await bot.change_presence(activity=discord.Game(name=".yardım  -  patrobot v1.0"))

#Yeni üye
"""@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hoşgeldin {member.name}. \n Eğer bize <#714143229364404314>ırsan Acemi rolünden kurtulabilirsin. Ayrıca diğer odalara da göz atmayı unutma :wink: \n Takıldığın herhangi bir şey olursa biz buradayız, <#713328432406200337>mekten çekinme. ')
"""

#Olaylar
@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    mesaj = ctx.content.lower()
    msj= mesaj.split()
    print(msj)

    if msj[0] == '.w':
        await wiki2.wikipediarama(ctx,msj)
    
    if msj[0] == ".s":
        del msj[0]
        kelimeuzunlugu = len(msj)
        print(kelimeuzunlugu)
        if kelimeuzunlugu == 1:
            print(msj[0])
            if msj[0] == "durdur":
                await pomodoro.durmaolayi(ctx)
            elif msj[0] == "tekrar":
                await pomodoro.yenizaman(ctx)
            elif msj[0] == "devam":
                await pomodoro.zamandevam(ctx)
            elif msj[0] == "iptal":
                await pomodoro.zamandurdurma(ctx)
            elif msj[0] == "şimdi":
                await pomodoro.anlikzaman(ctx)
            else:
                dakika = int(msj[0])
                if dakika > 720:
                    baslik = "Hey %r 720 dakikadan daha fazla bir süre tutamazsınız." %(ctx.author.mention)
                    embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
                    #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                    await ctx.channel.send(embed=embed)
                elif dakika < 1:
                    baslik = "Hey %r 1 dakikadan daha az süre tutamazsınız." %(ctx.author.mention)
                    embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
                    #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                    await ctx.channel.send(embed=embed)
                else:
                    saniye = int(dakika*60)
                    print(saniye)
                    await pomodoro.starter(ctx, dakika)

        else:
            pass
    
    if msj[0] == ".ist": #İstatistik
        await yardim.yardımkomut(ctx)

    if msj[0] == ".yardım": #Yardım
        del msj[0]
        kelimeuzunlugu = len(msj)
        print(kelimeuzunlugu)
        if kelimeuzunlugu == 0:
            await yardim.komutlar(ctx)
        elif kelimeuzunlugu == 1:
            if msj[0] == "s":
                await yardim.sayr(ctx)
            if msj[0] == "w":
                await yardim.wayr(ctx)
        else: 
            pass
    
    if msj[0] == ".geliştirme":
        print("Yapım aşamasında")

    else:
        pass

bot.run("NzU0NzA4NjUyNzA2NzU4NzI4.X14rNA.RO-VbaI1TnVZUTD2Yveri1DEGnM")
