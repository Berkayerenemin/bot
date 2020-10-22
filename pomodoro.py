import discord 
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot
import time as t
import asyncio

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
                    #yaz = "Kalan zaman:",timeformat
                    #await bot.change_presence(activity=discord.Game(name=yaz))
                    embed=discord.Embed(title="Süre Bitti",color=0xe26522)
                    #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                    etiket = ctx.author.mention
                    await ctx.channel.send(etiket)
                    await ctx.channel.send(embed=embed)
                    anlıkzaman.pop(kullaniciid)
                    kisidurdumu[kullaniciid] = "durdu"
                    break
                else:
                    kisidurdumu[kullaniciid] = "devam"
                
            elif calismalistesi[kullaniciid] == 0: #İptal etme özelliği
                tekraredildimi[kullaniciid] = 0
                baslik = "Süreniz iptal edildi. [%r] " %(ctx.author.name)
                embed=discord.Embed(title="İptal Edildi",description=baslik, color=0xe26522)
                #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                etiket = ctx.author.mention
                await ctx.channel.send(etiket)
                await ctx.channel.send(embed=embed)
                if kullaniciid in anlıkzaman:
                    anlıkzaman.pop(kullaniciid)
                    print(anlıkzaman.items())
                    tekraredildimi[kullaniciid] = 1
                    kisidurdumu[kullaniciid] = "iptal"
                else:
                    print("Hata kodu: 12")
                    tekraredildimi[kullaniciid] = 0
                    pass
                break 
                print("Zaman iptal edildi.")

            elif calismalistesi[kullaniciid] == 2: #Durdurma özelliği
                tekraredildimi[kullaniciid] = 0
                yenisaniye = anlıkzaman[kullaniciid]
                if yenisaniye > 60:
                    kalansure = int(yenisaniye/60)
                    baslik = "Kalan süre %r dakika [%r]" %(kalansure, ctx.author.mention)
                    embed=discord.Embed(title="Durduruldu",description=baslik, color=0x5699e1)
                    #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                    await ctx.channel.send(embed=embed)
                if yenisaniye <= 60:
                    baslik = "Kalan süre %r saniye [%r]" %(yenisaniye, ctx.author.mention)
                    embed=discord.Embed(title="Durduruldu",description=baslik, color=0x5699e1)
                    #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                    await ctx.channel.send(embed=embed)
                kisidurdumu[kullaniciid] = "durdu"
                break

            else:
                print("Herhangi bir işlem yapılmadı.")
                print("Hata kodu: 13")
    else:
        print("Çalışmıyor.")
        print("Hata kodu: 14")

async def starter(ctx, dakika):
    kullaniciid = ctx.author.id 
    if kullaniciid in anlıkzaman: #Şu an aktif süre var.
        baslik = "Süre zaten devam ediyor. [%r]" %(ctx.author.mention)
        embed= discord.Embed(title="Hata",description=baslik, color=0xff0000)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        #embed.set_footer(text="!s iptal ile süreyi iptal edebilirsiniz.")
        await ctx.channel.send(embed=embed)
        kisidurdumu[kullaniciid] = "devam"
        tekraredildimi[kullaniciid] = 0

    else: #İlk kez süre tutulacak.
        calismalistesi[kullaniciid] = 1 
        baslik = "Kalan süre: %r dakika! [%r] " %(dakika, ctx.author.mention)
        embed=discord.Embed(title="Başlatıldı",description=baslik,color=0x4ce141)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        #embed.set_footer(text=".s iptal ile süreyi durdurabilirsiniz.")
        await ctx.channel.send(embed = embed)
        sn = int(dakika*60)
        await zamanlayici(ctx, sn)

async def zamandurdurma(ctx):
    kullaniciid = ctx.author.id
    if kullaniciid in kisidurdumu and kisidurdumu[kullaniciid] == "iptal":
        baslik = "Şu an aktif süreniz yok! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        #embed.set_footer(text="!s {dakika} ile süre ayarlayabilirsiniz.")
        await ctx.channel.send(embed=embed)

    elif kullaniciid in kisidurdumu and kisidurdumu[kullaniciid] == "durdu":
        baslik = "Durdurulan süre iptal edildi. [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="İptal Edildi",description=baslik, color=0xff0000)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        #embed.set_footer(text="!s {dakika} ile süre ayarlayabilirsiniz.")
        await ctx.channel.send(embed=embed)
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
        calismalistesi[kullaniciid] = 0

async def durmaolayi(ctx):
    kullaniciid = ctx.author.id
    if kullaniciid in anlıkzaman:
        if kisidurdumu[kullaniciid] == "durdu":
            print(kisidurdumu.items())
            baslik = "Süre zaten durduruldu! [%r]" %(ctx.author.mention)
            embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
            #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
            #embed.set_footer(text="!s devam ile yeni süre oluşturabilirsiniz.")
            await ctx.channel.send(embed=embed)
            tekraredildimi[kullaniciid] = 0
        elif kisidurdumu[kullaniciid] == "iptal":
            baslik = "Süre zaten iptal edilmiş! [%r]" %(ctx.author.mention)
            embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
            #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
            #embed.set_footer(text="!s devam ile yeni süre oluşturabilirsiniz.")
            await ctx.channel.send(embed=embed)
            tekraredildimi[kullaniciid] = 1
        else:
            calismalistesi[kullaniciid] = 2
            tekraredildimi[kullaniciid] = 0
    else:
        baslik = "Süre zaten devam ediyor! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        #embed.set_footer(text="!s {dakika} ile yeni süre oluşturabilirsiniz.")
        await ctx.channel.send(embed=embed)
        tekraredildimi[kullaniciid] = 1

async def zamandevam(ctx):
    kullaniciid = ctx.author.id
    if kisidurdumu[kullaniciid] == "durdu": #Eğer durdurulmuşsa yap.
        sure = anlıkzaman[kullaniciid]
        baslik = "Hey %r senin için ayarladığım süre devam ediyor!" %(ctx.author.mention)
        embed=discord.Embed(title="Devam Ediyor",description=baslik, color=0x4ce141)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        await ctx.channel.send(embed=embed)
        calismalistesi[kullaniciid] = 1
        kisidurdumu[kullaniciid] = "devam"
        await zamanlayici(ctx, sure)
    
    elif kisidurdumu[kullaniciid]== "iptal": #Eğer iptal edilmişse yap.
        baslik = "Durdurulmuş bir süre yok! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        await ctx.channel.send(embed=embed)

    elif kisidurdumu[kullaniciid] == "devam": #Zaten devam ediliyorsa yap.
        baslik = "Süre zaten devam ediyor. [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Devam Edemedi",description=baslik, color=0x5699e1)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        await ctx.channel.send(embed=embed)

    else: #Daha hiç bir süre vs. tutmamışsa...
        baslik = "Önce bir süre ayarlamalısın. [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Devam Edemedi",description=baslik, color=0x5699e1)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        await ctx.channel.send(embed=embed)
    
async def yenizaman(ctx):
    kullaniciid = ctx.author.id
    if tekraredildimi[kullaniciid] == 0:
        baslik = "Şuanda tekrar özelliğini kullanamazsınız! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
        await ctx.channel.send(embed=embed)

    elif tekraredildimi[kullaniciid] == 1:
        if kullaniciid in ensonbelirlenensure:
            yenisaniye = ensonbelirlenensure[kullaniciid]
            print(ensonbelirlenensure.items())
            calismalistesi[kullaniciid] = 1
            baslik = "En son kullandığın süreyi ayarladım. [%r]" %(ctx.author.mention)
            embed=discord.Embed(title="Tekrar Ediyor",description=baslik, color=0xe26522)
            #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
            await ctx.channel.send(embed=embed)
            await zamanlayici(ctx, yenisaniye)
        else:
            print(ensonbelirlenensure.items())
            baslik = "Daha hiç süre ayarlamadınız! [%r]" %(ctx.author.mention)
            embed=discord.Embed(title="Tekrar Edemedi",description=baslik, color=0x5699e1)
            #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
            await ctx.channel.send(embed=embed)
    else:
        print("Hata kodu: 15")
        pass

async def anlikzaman(ctx):
    kullaniciid = ctx.author.id
    if kullaniciid in anlıkzaman:
            yenisaniye = anlıkzaman[kullaniciid]
            if yenisaniye > 60:
                kalansure = int(yenisaniye/60)
                baslik = "Kalan süre %r dakika [%r]" %(kalansure, ctx.author.mention)
                embed=discord.Embed(title="Anlık Süre",description=baslik, color=0x5699e1)
                #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                await ctx.channel.send(embed=embed)
            if yenisaniye <= 60:
                baslik = "Kalan süre %r saniye [%r]" %(yenisaniye, ctx.author.mention)
                embed=discord.Embed(title="Anlık Süre",description=baslik, color=0x5699e1)
                #embed.set_thumbnail(url="https://media.giphy.com/media/T1zgJ7cp8tWla/source.gif")
                await ctx.channel.send(embed=embed)

    else:
        print("Hata kodu: 16")
        pass