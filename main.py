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


import wikipedia
wikipedia.set_lang("tr")

@bot.command()
async def wiki(ctx, *,words):
    print(words)
    ad = wikipedia.summary(words, sentences=2)
    kelime = "Aradığınız konu: "+words
    embed=discord.Embed(title=kelime, description=ad, color=0xdd2c2c)
    embed.set_author(name="Wikipedia", url="https://tr.wikipedia.org/", icon_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fthumb%2F8%2F80%2FWikipedia-logo-v2.svg%2F1200px-Wikipedia-logo-v2.svg.png&f=1&nofb=1")
    embed.set_footer(text="!komutlar yazarak komut listesine ulaşabilirsiniz.")
    await ctx.channel.send(embed=embed)

@bot.command(aliases=['neredeyim'])
async def yardım(ctx):
    embed=discord.Embed(title="Yardım / Help", description="!komutlar ile sahip olduğum özellikleri tek bir listede görüntüleyebilirsin.")
    embed.set_author(name="Enigma")
    embed.add_field(name="Dil:", value="%100 Türkçe", inline=False)
    embed.add_field(name="Yazılım:", value="Açık Kaynak (Github)", inline=False)
    embed.add_field(name="Yüklenmiş Özellik Sayısı:", value="5", inline=False)
    embed.add_field(name="Bulunan Sunucu Sayısı:", value="4", inline=True)
    embed.set_footer(text="Enigma, Python dili ile yazılmış açık kaynaklı bir Discord botudur.")
    await ctx.channel.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members =True)
async def sunucudanat(ctx,member : discord.Member, *, reason="Herhangi bir nedeni yok."):
    await member.send("Yönetici tarafından sunucudan atıldınız. Çünkü:"+reason)
    await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(ban_members = True)
async def banla(ctx,member : discord.Member, *, reason="Herhangi bir nedeni yok"):
    await ctx.channel.send("@"+ member.name + " sunucudan sonsuza kadar uzaklaştırıldı. Onsuz bir sunucu herkes için daha iyi olacak.")
    await member.ban(reason=reason)

@bot.command()
async def p(ctx,iss,seconds,member : discord.Member):
    print(seconds)
    sec = int(seconds)
    member3 = str(member.id)
    a= "<@"+ member3 +"> pomodoro aktif.."
    await ctx.channel.send(a)
    while sec:
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        print(timeformat, end='\r')
        yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
        #times = (timeformat, end='\r')
        await bot.change_presence(activity=discord.Game(name=yaz))
        await asyncio.sleep(5)
        sec -= 5
        if sec <= 0:
            timeformat = '{:02d}:{:02d}'.format(minn, secc)
            print(timeformat, end='\r')
            yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
            await bot.change_presence(activity=discord.Game(name=yaz))
            break
        else:
            pass
    await asyncio.sleep(1)
    print("bitti")
    member2 = str(member.id)
    d= "<@"+ member2 +"> pomodoro sona erdi."
    await ctx.channel.send(d)
bot.run(to+ke+n)
