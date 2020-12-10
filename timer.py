import datetime
import asyncio
import discord

async def ykszaman():
    bugun = datetime.date.today()
    print(bugun)
    yıl = 2021
    ay = 6
    gün = 18
    hedef = datetime.date(year=yıl, month=ay, day=gün)
    print(hedef)
    
    gunfarkı = hedef - bugun
    return gunfarkı.days
