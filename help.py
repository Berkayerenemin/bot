import discord
async def yardımkomut(ctx):
    embed=discord.Embed(title="Yardım / Help", description="!komutlar ile sahip olduğum özellikleri tek bir listede görüntüleyebilirsin.")
    embed.set_author(name="Enigma")
    embed.add_field(name="Dil:", value="%100 Türkçe", inline=False)
    embed.add_field(name="Yazılım:", value="Açık Kaynak (Github)", inline=False)
    embed.add_field(name="Yüklenmiş Özellik Sayısı:", value="5", inline=False)
    embed.add_field(name="Bulunan Sunucu Sayısı:", value="4", inline=True)
    embed.set_footer(text="Enigma, Python dili ile yazılmış açık kaynaklı bir Discord botudur.")
    await ctx.channel.send(embed=embed)

async def ban(ctx, member, reason):
    await ctx.channel.send("@"+ member.name + " sunucudan sonsuza kadar uzaklaştırıldı. Onsuz bir sunucu herkes için daha iyi olacak.")
    await member.ban(reason=reason)

async def at(ctx, member, reason):
    await member.send("Yönetici tarafından sunucudan atıldınız. Çünkü:"+reason)
    await member.kick(reason=reason)