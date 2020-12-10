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
import timer

token = os.environ.get('BOT-TOKEN')
role_id = 782853573402558504
nefer_id = 782254293877129218
ustad_id = 782214988591792149
mico_id = 782215314611765289
say_id = 782294101994504242
everyone_id = 782214393949454349
ea_id = 782375578305167414
roles = {}
roller = []

#Bot prefix
bot = commands.Bot(command_prefix='.')

#Açılış
@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    print(f'{bot.user.id} sunucuda...')
    a = await timer.ykszaman()
    b = str(a)
    yazi = ".yardım - YKS'ye kalan: " + b
    await bot.change_presence(activity=discord.Game(name=yazi))

#Yeni üye
"""@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hoşgeldin {member.name}. \n Eğer bize <#782349088539934771>ırsan, üstad arakadaşlarımızın onayalamasından sonra Miço rolünü alabilirsin. Ayrıca diğer odalara da göz atmayı unutma :wink: \n Takıldığın herhangi bir şey olursa biz buradayız, <#782262043884781598> etmekten çekinme. ')
"""

@bot.event
async def on_voice_state_update(member, before, after):
    roleodak = discord.utils.get(member.guild.roles, id=role_id)
    rolenefer = discord.utils.get(member.guild.roles, id=nefer_id)
    roleustad = discord.utils.get(member.guild.roles, id=ustad_id)
    rolemico = discord.utils.get(member.guild.roles, id=mico_id)
    rolesay = discord.utils.get(member.guild.roles, id=say_id)
    roleeveryone = discord.utils.get(member.guild.roles, id=everyone_id)
    rolea = discord.utils.get(member.guild.roles, id=ea_id)
    if before.channel is None and after.channel is not None:
        #role =discord.utils.get(member.guild.roles, name="focus")
        #await member.add_roles(role)
        #await member.guild.system_channel.send("Alarm!")
        if after.channel.id == 782214394884653059:
            await member.add_roles(roleodak)
            for role in member.roles:
                roller.append(role.id)
                if role.id == 782214988591792149:
                    await member.remove_roles(roleustad)
                elif role.id == 782294101994504242:
                    await member.remove_roles(rolesay)
                elif role.id == 782254293877129218:
                    await member.remove_roles(rolenefer)
                elif role.id == 782375578305167414:
                    await member.remove_roles(rolea)
                elif role.id == 782215314611765289:
                    await member.remove_roles(rolemico)
            roles[member.id] = roller
        else:
            await member.remove_roles(role)

    elif before.channel is not None and after.channel is not None:
        if after.channel.id == 782214394884653059:
            await member.add_roles(roleodak)
            for role in member.roles:
                roller.append(role.id)
                print(role.id)
                if role.id == 782214988591792149:
                    await member.remove_roles(roleustad)
                elif role.id == 782294101994504242:
                    await member.remove_roles(rolesay)
                elif role.id == 782254293877129218:
                    await member.remove_roles(rolenefer)
                elif role.id == 782375578305167414:
                    await member.remove_roles(rolea)
                elif role.id == 782215314611765289:
                    await member.remove_roles(rolemico)
        else:
            await member.remove_roles(role)

    elif before.channel is not None and after.channel is None:
        if before.channel.id == 782214394884653059:
            rollist = roles[member.id]
            for role in rollist:
                if role == 782214988591792149:
                    await member.add_roles(roleustad)
                elif role == 782294101994504242:
                    await member.add_roles(rolesay)
                elif role == 782254293877129218:
                    await member.add_roles(rolenefer)
                elif role == 782375578305167414:
                    await member.add_roles(rolea)
                elif role == 782215314611765289:
                    await member.add_roles(rolemico)
            await member.remove_roles(role)
            roles.pop(member.id)
        else:
            pass
    elif before.channel is not None and after.channel is not None:
        if before.channel.id == 782214394884653059:
            rollist = roles[member.id]
            print("Sorun", rollist)
            for role in rollist:
                if role == 782214988591792149:
                    await member.add_roles(roleustad)
                elif role == 782294101994504242:
                    await member.add_roles(rolesay)
                elif role == 782254293877129218:
                    await member.add_roles(rolenefer)
                elif role == 782375578305167414:
                    await member.add_roles(rolea)
                elif role == 782215314611765289:
                    await member.add_roles(rolemico)
            await member.remove_roles(roleodak)
            roles.pop(member.id)
        else:
            pass
    else:
        pass

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
        embed=discord.Embed(title="Geliştirici Günlüğü - Gelecek", color=0xd81818)
        embed.add_field(name="Geri Bildirim Mekanizması", value=".gb", inline=False)
        embed.add_field(name="To-Do List Özelliği", value=".todo", inline=False)
        embed.add_field(name="Müzik Çalma Özelliği", value=".m", inline=False)
        await ctx.channel.send(embed=embed)
    else:
        pass

bot.run(token)
