import discord 
import os
import random
import sqlite3
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio

bot = commands.Bot(command_prefix='!')

minWork=25
maxWork=720
minSpring=1
maxSpring=2
minWorkRatio=5

pomodorodata = {}

def datayayaz(id, sonzaman):
    if id in pomodorodata:
        pomodorodata.pop(id)
        pomodorodata[id] = sonzaman
    else:
        pomodorodata[id] = sonzaman

async def zamanlama(ctx,iss,seconds):
    print(seconds)
    sec = int(seconds)
    embed=discord.Embed(title="Pomodoro",description=ctx.author.mention, color=0x1fb731)
    embed.set_author(name="Enigma Bot")
    embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
    embed.add_field(name="AKTİF", value="Boş zaman yoktur; boşa geçen zaman vardır.", inline=True)
    datayayaz(ctx.author.id, seconds)
    await ctx.channel.send(embed=embed)
    print(pomodorodata.items())
    while sec:
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        print(timeformat, end='\r')
        #times = timeformat, end='\r'
        yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
        await asyncio.sleep(5)
        sec -= 5
        if sec <= 0:
            timeformat = '{:02d}:{:02d}'.format(minn, secc)
            print(timeformat, end='\r')
            yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
            break
        else:
            pass
    await asyncio.sleep(1)
    print("bitti")
    embed=discord.Embed(title="Pomodoro",description=ctx.author.mention, color=0x1fb731)
    embed.set_author(name="Enigma Bot")
    embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
    embed.add_field(name="PASİF", value="Boş zaman yoktur; boşa geçen zaman vardır.", inline=True)
    await ctx.channel.send(embed=embed)
    print(pomodorodata)


async def zamanlama2(ctx):
    member4 = ctx.author.id
    print(pomodorodata.items())
    if member4 in pomodorodata:
        print(pomodorodata[member4])
        seconds2 = pomodorodata[member4]
        sec = int(seconds2)
        embed=discord.Embed(title="Pomodoro",description=ctx.author.mention, color=0x1fb731)
        embed.set_author(name="Enigma Bot")
        embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        embed.add_field(name="AKTİF", value="Boş zaman yoktur; boşa geçen zaman vardır.", inline=True)
        await ctx.channel.send(embed=embed)
        while sec:
            minn, secc = divmod(sec, 60)
            timeformat = '{:02d}:{:02d}'.format(minn, secc)
            print(timeformat, end='\r')
            #yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
            #times = (timeformat, end='\r')
            #await bot.change_presence(activity=discord.Game(name=yaz))
            await asyncio.sleep(5)
            sec -= 5
            if sec <= 0:
                timeformat = '{:02d}:{:02d}'.format(minn, secc)
                print(timeformat, end='\r')
                #yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
                #await bot.change_presence(activity=discord.Game(name=yaz))
                break
            else:
                pass
        await asyncio.sleep(1)
        print("bitti")
        #await bot.change_presence(activity=discord.Game(name="Ich bin Enigma"))
        embed=discord.Embed(title="Pomodoro",description=ctx.author.mention, color=0x1fb731)
        embed.set_author(name="Enigma Bot")
        embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        embed.add_field(name="PASİF", value="Boş zaman yoktur; boşa geçen zaman vardır.", inline=True)
        await ctx.channel.send(embed=embed)
        print(pomodorodata)

    else:
        c= "Daha önce hiç pomodoro özelliğini kullanmamışsınız."
        await ctx.channel.send(c)


#verileri database'e yazma
#insert = "INSERT INTO pomodoroveri (userid, sonzaman) VALUES(?,?)"
#c.execute(insert, [(id),(sonz)])
#db.commit()


#aut değişkeni içindeki değeri arama
#read = c.execute("SELECT * FROM user WHERE username='{}'".format(aut))
#for pgn in read.fetchall():
#print(pgn)