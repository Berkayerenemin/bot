import discord 

def metinyayimlama(kod, sure, ctx):
    print(kod)
    if kod == 1:
        print("Başlatıldı!")
        baslik = "Kalan süre: %r dakika! [%r] " %(sure, ctx.author.mention)
        embed=discord.Embed(title="Başlatıldı",description=baslik,color=0x4ce141)
        return embed
    elif kod == 2:
        print("Başlatma Hatası!")
        baslik = "Süre zaten devam ediyor. [%r]" %(ctx.author.mention)
        embed= discord.Embed(title="Hata",description=baslik, color=0xff0000)
        return embed
    elif kod == 3:
        embed=discord.Embed(title="Süre Bitti",color=0xe26522)
        return embed
    elif kod == 4:
        baslik = "Süreniz iptal edildi. [%r] " %(ctx.author.name)
        embed=discord.Embed(title="İptal Edildi",description=baslik, color=0xe26522)
        return embed
    elif kod == 5:
        baslik = "Kalan süre %r dakika [%r]" %(sure, ctx.author.mention)
        embed=discord.Embed(title="Durduruldu",description=baslik, color=0x5699e1)
        return embed
    elif kod == 6:
        baslik = "Kalan süre %r saniye [%r]" %(sure, ctx.author.mention)
        embed=discord.Embed(title="Durduruldu",description=baslik, color=0x5699e1)
        return embed
    elif kod == 7:
        baslik = "Şu an aktif süreniz yok! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        return embed
    elif kod == 8:
        baslik = "Durdurulan süre iptal edildi. [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="İptal Edildi",description=baslik, color=0xff0000)
        return embed
    elif kod == 9:
        baslik = "Süre zaten durduruldu! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        return embed
    elif kod == 10:
        baslik = "Süre zaten iptal edilmiş! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        return embed
    elif kod == 11:
        baslik = "Aktif bir süren yok! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        return embed
    elif kod == 12:
        baslik = "Kalan süre %r dakika [%r]" %(sure, ctx.author.mention)
        embed=discord.Embed(title="Devam Ediyor",description=baslik, color=0x4ce141)
        return embed
    elif kod == 13:
        baslik = "Kalan süre %r saniye [%r]" %(sure, ctx.author.mention)
        embed=discord.Embed(title="Devam Ediyor",description=baslik, color=0x4ce141)
        return embed
    elif kod == 14:
        baslik = "Durdurulmuş bir süre yok! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        return embed
    elif kod == 15:
        baslik = "Süre zaten devam ediyor. [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Devam Edemedi",description=baslik, color=0x5699e1)
        return embed
    elif kod == 16:
        baslik = "Önce bir süre ayarlamalısın. [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Devam Edemedi",description=baslik, color=0x5699e1)
        return embed
    elif kod == 17:
        baslik = "Şuanda tekrar özelliğini kullanamazsınız! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Hata",description=baslik, color=0xff0000)
        return embed
    elif kod == 18:
        baslik = "En son kullandığın süreyi ayarladım. [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Tekrar Ediyor",description=baslik, color=0xe26522)
        return embed
    elif kod == 19:
        baslik = "Daha hiç süre ayarlamadınız! [%r]" %(ctx.author.mention)
        embed=discord.Embed(title="Tekrar Edemedi",description=baslik, color=0x5699e1)
        return embed
    elif kod == 20:
        baslik = "Kalan süre %r dakika [%r]" %(sure, ctx.author.mention)
        embed=discord.Embed(title="Anlık Süre",description=baslik, color=0x5699e1)
        return embed
    elif kod == 21:
        baslik = "Kalan süre %r saniye [%r]" %(sure, ctx.author.mention)
        embed=discord.Embed(title="Anlık Süre",description=baslik, color=0x5699e1)
        return embed
    else:
        pass