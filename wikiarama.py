#wikipedia.py
import wikipedia
import json
import discord

wikipedia.set_lang("tr")

async def wikipediarama(ctx,words):
    print(words)
    ad = wikipedia.summary(words, sentences=2)
    kelime = "Aradığınız konu: "+words
    embed=discord.Embed(title=kelime, description=ad, color=0xdd2c2c)
    embed.set_author(name="Wikipedia", url="https://tr.wikipedia.org/", icon_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fthumb%2F8%2F80%2FWikipedia-logo-v2.svg%2F1200px-Wikipedia-logo-v2.svg.png&f=1&nofb=1")
    embed.set_footer(text="!komutlar yazarak komut listesine ulaşabilirsiniz.")
    await ctx.channel.send(embed=embed)
