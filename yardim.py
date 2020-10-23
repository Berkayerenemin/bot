import discord
from datetime import datetime
#timestamp=datetime.utcnow()
async def yardımkomut(ctx):
    embed=discord.Embed(title="İstatikler", color=0xd81818)
    embed.set_author(name="patrobot")
    embed.add_field(name="Dil:", value="%100 Türkçe", inline=False)
    embed.add_field(name="Yazılım:", value="Python Açık Kaynak(Github)", inline=False)
    embed.add_field(name="Yüklenmiş Özellik Sayısı:", value="5", inline=False)
    embed.add_field(name="Bulunan Sunucu Sayısı:", value="4", inline=True)
    embed.set_footer(text="Patrobot, Python dili ile yazılmış açık kaynaklı bir Discord botudur.")
    await ctx.channel.send(embed=embed)

async def ban(ctx, member, reason):
    await ctx.channel.send("@"+ member.name + " sunucudan sonsuza kadar uzaklaştırıldı. Onsuz bir sunucu herkes için daha iyi olacak.")
    await member.ban(reason=reason)

async def at(ctx, member, reason):
    await member.send("Yönetici tarafından sunucudan atıldınız. Çünkü:"+reason)
    await member.kick(reason=reason)


async def komutlar(ctx):
    embed=discord.Embed(title="Komutlar / Commands", color=0xd81818)
    embed.add_field(name="Süre Tutma / Tekrar / İptal Özelliği:", value=".yardım s", inline=False)
    embed.add_field(name="Wikipedia Özelliği:", value=".yardım w", inline=False)
    embed.add_field(name="İstatiksel Veri:", value=".ist", inline=False)
    await ctx.channel.send(embed=embed)


async def sayr(ctx):
    embed=discord.Embed(title="Süre Tutma / Tekrar / İptal Özelliği", description="Süre tutma özelliği oldukça basittir. Süre miktarını girersiniz ve ben bunu aklımda tutarım. Süre bittiğinde ise size bildirim gönderirim. Dilersen süreyi durdurabilirsin, sonrasında ise aynı yerden tutmaya devam edebilirim.", color=0xd81818)
    embed.add_field(name="Süre Tutmak İçin:", value=".s {dakika}", inline=False)
    embed.add_field(name="Kalan Süreyi Görüntülemek İçin:", value=".s şimdi", inline=False)
    embed.add_field(name="Aktif Olan Süre İptali İçin:", value=".s iptal", inline=False)
    embed.add_field(name="Sureyi Durdurmak İçin:", value=".s durdur", inline=False)
    embed.add_field(name="Durdurulan Süreyi Devam Ettirmek İçin:", value=".s devam", inline=False)
    embed.add_field(name="En Son Tutulan Süreyi Tekrar Tutmak İçin:", value=".s tekrar", inline=False)
    embed.add_field(name="Ayrıntılı Video:", value="https://bit.ly/2IWcJE1", inline=False)
    await ctx.channel.send(embed=embed)


async def wayr(ctx):
    embed=discord.Embed(title="Wikipedia Özelliği",description="Bir kelimenin veya cümlenin anlamını, işleyişini merak ettiysen sakın durma. Wikipedia'da arama özelliği ile anında ara. Eğer aramana rağmen karşına bir sonuç çıkartamadıysam bil ki aklım karışmıştır. O zaman aradığın kelimeyi daha ayrıntılı yazıp aratman gerekir.", color=0xd81818)
    embed.add_field(name="Wikipedia'da Aramak İçin:", value=".w {aranacak kelime}", inline=False)
    await ctx.channel.send(embed=embed)