import discord 
import os
import random
import sqlite3
from discord.ext import commands
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
    pomodorodata[id] = sonzaman

async def zamanlama(ctx,iss,seconds,member):
    print(seconds)
    sec = int(seconds)
    member3 = str(member.id)
    a= "<@"+ member3 +"> pomodoro aktif.."
    datayayaz(member3, seconds)
    await ctx.channel.send(a)
    print(pomodorodata.items())
    while sec:
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        print(timeformat, end='\r')
        yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
        #times = (timeformat, end='\r')
        #await bot.change_presence(activity=discord.Game(name=yaz))
        await asyncio.sleep(5)
        sec -= 5
        if sec <= 0:
            timeformat = '{:02d}:{:02d}'.format(minn, secc)
            print(timeformat, end='\r')
            yaz = "Şunun için çalışılıyor: "+iss+" "+timeformat
            #await bot.change_presence(activity=discord.Game(name=yaz))
            break
        else:
            pass
    await asyncio.sleep(1)
    print("bitti")
    member2 = str(member.id)
    #await bot.change_presence(activity=discord.Game(name="Ich bin Enigma"))
    d= "<@"+ member2 +"> pomodoro sona erdi."
    await ctx.channel.send(d)
    print(pomodorodata)


async def zamanlama2(ctx, member):
    member4 = str(member.id)
    print(pomodorodata.items())
    if member4 in pomodorodata:
        print(pomodorodata[member4])
        seconds2 = pomodorodata[member4]
        sec = int(seconds2)
        a= "<@"+ member4 +"> pomodoro aktif.. (En son kullandığınız zaman baz alınmıştır)"
        await ctx.channel.send(a)
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
        d= "<@"+ member4 +"> pomodoro sona erdi."
        await ctx.channel.send(d)
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