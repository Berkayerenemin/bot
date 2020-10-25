import discord 
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot
import time as t
import asyncio
import pomodeg

ensonbelirlenensure = {} #Tekrar için gerekli 
anlıkzaman = {} #Durdurmadan sonra zamanı başlatmansı/ anlık komutu için gerekli.
calismalistesi = {} # Zaman tutuluyor: 1      Zamanı iptal etti: 0      Zamanı durdurdu: 2
kisidurdumu = {} #Durdurma başarılı ise: "durdu"    İptal edilme başarılı ise: "iptal"    Devam edilme başarılı ise: "devam" 
tekraredildimi = {} #Tekrar edilebilir ise 1 edemez 0 olsun.


def sonzamaniisle(id, sonzaman):
    if id in ensonbelirlenensure:
        ensonbelirlenensure.pop(id)
        ensonbelirlenensure[id] = sonzaman
    else:
        ensonbelirlenensure[id] = sonzaman

async def zamanlayici(ctx, saniye):
    kullaniciid = ctx.author.id 
    dakika = int(saniye/60)
    if calismalistesi[kullaniciid] == 1:
        sonzamaniisle(kullaniciid, saniye)
        while saniye:
            if calismalistesi[kullaniciid] == 1: #Süre tutma özelliği
                tekraredildimi[kullaniciid] = 0
                minn, secc = divmod(saniye, 60)
                timeformat = '{:02d}:{:02d}'.format(minn, secc)
                print(timeformat, end='\r')
                await asyncio.sleep(1)
                saniye -= 1
                anlıkzaman[kullaniciid] = saniye
                if saniye == 0:
                    timeformat = '{:02d}:{:02d}'.format(minn, secc)
                    print(timeformat, end='\r')
                    etiket = ctx.author.mention
                    await ctx.channel.send(etiket)
                    await ctx.channel.send(embed=pomodeg.metinyayimlama(3, saniye, ctx))
                    anlıkzaman.pop(kullaniciid)
                    kisidurdumu[kullaniciid] = "iptal"
                    tekraredildimi[kullaniciid] = 1
                    break
                else:
                    kisidurdumu[kullaniciid] = "devam"
                
            elif calismalistesi[kullaniciid] == 0: #İptal etme özelliği
                tekraredildimi[kullaniciid] = 0
                etiket = ctx.author.mention
                await ctx.channel.send(etiket)
                await ctx.channel.send(embed=pomodeg.metinyayimlama(4, 0, ctx))
                if kullaniciid in anlıkzaman:
                    anlıkzaman.pop(kullaniciid)
                    print(anlıkzaman.items())
                    tekraredildimi[kullaniciid] = 1
                    kisidurdumu[kullaniciid] = "iptal"
                else:
                    print("Hata kodu: 12")
                    tekraredildimi[kullaniciid] = 0
                    pass

                print("Zaman iptal edildi.")
                break 

            elif calismalistesi[kullaniciid] == 2: #Durdurma özelliği
                tekraredildimi[kullaniciid] = 0
                yenisaniye = anlıkzaman[kullaniciid]
                if yenisaniye > 60:
                    kalansure = int(yenisaniye/60)
                    kisidurdumu[kullaniciid] = "durdu"
                    await ctx.channel.send(embed=pomodeg.metinyayimlama(5, kalansure, ctx))
                elif yenisaniye <= 60:
                    await ctx.channel.send(embed=pomodeg.metinyayimlama(6, yenisaniye, ctx))
                    kisidurdumu[kullaniciid] = "durdu"
                break

            else:
                print("Herhangi bir işlem yapılmadı.")
                print("Hata kodu: 13")
    else:
        print("Çalışmıyor.")
        print("Hata kodu: 14")

async def starter(ctx, dakika): #Başlangıç :)
    kullaniciid = ctx.author.id 
    if kullaniciid in anlıkzaman: #Şu an aktif süre var.
        if kisidurdumu[kullaniciid] == "durdu":
            await ctx.channel.send(embed=pomodeg.metinyayimlama(9, 0, ctx))

        else:
            await ctx.channel.send(embed=pomodeg.metinyayimlama(2, dakika, ctx))
            kisidurdumu[kullaniciid] = "devam"
            tekraredildimi[kullaniciid] = 0

    else: #İlk kez süre tutulacak.
        calismalistesi[kullaniciid] = 1 
        await ctx.channel.send(embed=pomodeg.metinyayimlama(1, dakika, ctx))
        sn = int(dakika*60)
        kisidurdumu[kullaniciid] = "devam"
        await zamanlayici(ctx, sn)

async def zamandurdurma(ctx):
    kullaniciid = ctx.author.id
    if kullaniciid in kisidurdumu and kisidurdumu[kullaniciid] == "iptal":
        await ctx.channel.send(embed=pomodeg.metinyayimlama(7, 0, ctx))

    elif kullaniciid in kisidurdumu and kisidurdumu[kullaniciid] == "durdu":
        await ctx.channel.send(embed=pomodeg.metinyayimlama(8, 0, ctx))
        if kullaniciid in anlıkzaman:
            anlıkzaman.pop(kullaniciid)
            print(anlıkzaman.items())
            tekraredildimi[kullaniciid] = 1
            kisidurdumu[kullaniciid] = "iptal"
        else:
            print("Hata kodu: 12")
            tekraredildimi[kullaniciid] = 0
            pass
    else:
        calismalistesi[kullaniciid] == 0
        kisidurdumu[kullaniciid] = "iptal"
        tekraredildimi[kullaniciid] = 1

async def durmaolayi(ctx):
    kullaniciid = ctx.author.id
    if kullaniciid in anlıkzaman:
        if kisidurdumu[kullaniciid] == "durdu":
            print(kisidurdumu.items())
            await ctx.channel.send(embed=pomodeg.metinyayimlama(9, 0, ctx))
            tekraredildimi[kullaniciid] = 0
        elif kisidurdumu[kullaniciid] == "iptal":
            await ctx.channel.send(embed=pomodeg.metinyayimlama(10, 0, ctx))
            tekraredildimi[kullaniciid] = 1
        else:
            calismalistesi[kullaniciid] = 2
            tekraredildimi[kullaniciid] = 0
    else:
        await ctx.channel.send(embed=pomodeg.metinyayimlama(11, 0, ctx))
        tekraredildimi[kullaniciid] = 1

async def zamandevam(ctx):
    kullaniciid = ctx.author.id
    if kisidurdumu[kullaniciid] == "durdu": #Eğer durdurulmuşsa yap.
        sure = anlıkzaman[kullaniciid]
        if sure > 60:
            kalansure = int(sure/60)
            await ctx.channel.send(embed=pomodeg.metinyayimlama(12, kalansure, ctx))
        elif sure <= 60:
            await ctx.channel.send(embed=pomodeg.metinyayimlama(13, sure, ctx))
        else: 
            pass
        calismalistesi[kullaniciid] = 1
        kisidurdumu[kullaniciid] = "devam"
        await zamanlayici(ctx, sure)
    
    elif kisidurdumu[kullaniciid]== "iptal": #Eğer iptal edilmişse yap.
        await ctx.channel.send(embed=pomodeg.metinyayimlama(14, 0, ctx))

    elif kisidurdumu[kullaniciid] == "devam": #Zaten devam ediliyorsa yap.
        await ctx.channel.send(embed=pomodeg.metinyayimlama(15, 0 , ctx))

    else: #Daha hiç bir süre vs. tutmamışsa...
        await ctx.channel.send(embed=pomodeg.metinyayimlama(16, 0 , ctx))
    
async def yenizaman(ctx):
    kullaniciid = ctx.author.id
    if tekraredildimi[kullaniciid] == 0:
        await ctx.channel.send(embed=pomodeg.metinyayimlama(17, 0 ,ctx))

    elif tekraredildimi[kullaniciid] == 1:
        if kullaniciid in ensonbelirlenensure:
            yenisaniye = ensonbelirlenensure[kullaniciid]
            print(ensonbelirlenensure.items())
            calismalistesi[kullaniciid] = 1
            await ctx.channel.send(embed=pomodeg.metinyayimlama(18, 0 ,ctx))
            await zamanlayici(ctx, yenisaniye)
        else:
            print(ensonbelirlenensure.items())
            await ctx.channel.send(embed=pomodeg.metinyayimlama(19, 0, ctx))
    else:
        print("Hata kodu: 15")
        pass

async def anlikzaman(ctx):
    kullaniciid = ctx.author.id
    if kullaniciid in anlıkzaman:
            yenisaniye = anlıkzaman[kullaniciid]
            if yenisaniye > 60:
                kalansure = int(yenisaniye/60)
                await ctx.channel.send(embed=pomodeg.metinyayimlama(20, kalansure, ctx))
            if yenisaniye <= 60:
                await ctx.channel.send(embed=pomodeg.metinyayimlama(21, yenisaniye, ctx))

    else:
        print("Hata kodu: 16")
        pass