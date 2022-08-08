import discord
from time import sleep
from discord.ext import commands
from discord.ext import tasks
import asyncio
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from module.raspador_kabum import *
from module.data import *
import os

# from dotenv import load_dotenv
# load_dotenv()
# CLIENT_ID_TWITCH = os.getenv("CLIENT_ID_TWITCH")
# DISCORD_GUILD = os.getenv("DISCORD_GUILD")
# TOKEN_DISCORD = os.getenv("TOKEN_DISCORD")
# TWITCH_SECRET = os.getenv("TWITCH_SECRET")

CLIENT_ID_TWITCH = os.environ.get("CLIENT_ID_TWITCH")
DISCORD_GUILD = os.environ.get("DISCORD_GUILD")
TOKEN_DISCORD = os.environ.get("TOKEN_DISCORD")
TWITCH_SECRET = os.environ.get("TWITCH_SECRET")

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print('on ready')
    messages.start()
    #clips.start()
    #msgembed.start()

@tasks.loop(hours=1)
async def clips():

    inicio = hour()[0]
    fim = hour()[1]

    for key in streamers:
        print(key)
        #fim = '2022-04-01T00:00'
        #inicio = '2022-04-02T20:00'
        channel = bot.get_channel(902379408625647627)
        url = clipsHora(str(streamers[key]),str(fim),str(inicio),50,"trizspacca")
        print(url)
        for i in range(len(url)):
            msg = url[i]
            await channel.send(msg)
            sleep(5)

@bot.command()
async def clear(ctx, amount=0):

    print(amount)
    if ctx.author.guild_permissions.administrator:
        if amount > 0:
            print(amount,' valor do amount')
            await ctx.channel.purge(limit=amount)
            sucess = await ctx.send (f"{amount} messages has been deleted <a:white_check_mark:>") #sending success msg
            await asyncio.sleep(10)
            await sucess.delete()
        else:
            await ctx.send("You need to enter a number higher than 0")
    else:
        await ctx.send("You need to be an admin to use this command")

@bot.command(name='baixarclip')
async def downloadClips(ctx, url):
           
    AutCall = requests.post(url=authURL, params=AutParams) 
    access_token = AutCall.json()['access_token']

    head = {
    'Authorization' :  "Bearer " + access_token,
      'Client-ID' : CLIENT_ID_TWITCH,
    }
    url = url.replace("https://clips.twitch.tv/","")
    r = requests.get('https://api.twitch.tv/helix/clips?id={}'.format(url), headers = head).json()
    dicionario = r['data']
    mp4 = dicionario[0]['thumbnail_url']
    #mp4 = dicionario["thumbnail_url"]
    linkmp4 = mp4.replace("-preview-480x272.jpg",".mp4")
    await ctx.channel.purge(limit=1)
    download = await ctx.send(f"Clique no link para baixar o clip {linkmp4}")
    await asyncio.sleep(20)
    await download.delete()


@tasks.loop(seconds=20)
async def msgembed():

    channel = bot.get_channel(997599829423304785)
    embed = discord.Embed()
    data = load_data()
    produtos = data['produtos']
    await channel.purge(limit=len(produtos))
    for key in produtos:

        p = price_product(produtos[key])
        embed.description = "{}\n {}  [link]({}).".format(p[0], p[1],p[2])
        embed.set_thumbnail(url= p[3])
        await channel.send(embed=embed)
        await asyncio.sleep(1)

@bot.command()
async def manualpreco(ctx):
    embed = discord.Embed()
    data = load_data()
    produtos = data['produtos']
    #await channel.purge(limit=2)
    for key in produtos:

        p = price_product(produtos[key])
        embed.description = "{}\n {}  [link]({}).".format(p[0], p[1],p[2])
        embed.set_thumbnail(url= p[3])
        await ctx.send(embed=embed)
        await asyncio.sleep(1)
        

@bot.command()
async def mostralista(ctx):
    
    data = load_data()
    data = data['produtos']
    
    for item in data:
        await ctx.send(item)

@bot.command()
async def printlista(ctx):
    data = load_data()
    data = data['produtos']
    print(data)
    
@bot.command()
async def deletar(ctx):

    data = load_data()
    data = data['produtos']

    for item in data:
        if item in ctx.message.content:
            dicionario = removekey(data,item)
            temp = {'produtos':dicionario}
            salve_data(temp)
            
            await ctx.send(item+" deletado")

@bot.command()
async def add(ctx):

    data = load_data()
    produto = (ctx.message.content).split(" ")
    del produto[0]
    add_item(data,produto)

@tasks.loop(hours=6)
async def messages():
    c = bot.get_channel(997599829423304785)
    messages = await c.history(limit=None).flatten()
    embed = discord.Embed(color=0xFF5733)

    for message in messages:
        if message.author.name == "BeringelaClips":
            await message.delete()

        else:
            if message.content.startswith("https://www.kabum.com.br/produto/"):
                p = price_product(message.content)
                embed.title = p[0]
                embed.set_author(name="Kabum", url="https://www.kabum.com.br/", icon_url="https://sucodemanga.com.br/wp-content/uploads/2021/03/kabum-logo-150x.png")
                
                embed.description = "{} [Compre agora]({}).".format( p[1], p[2])
                
                await c.send(embed=embed)


@bot.command()
async def setimg(ctx):
    item = ((ctx.message.content).split(" "))[1]
    url_image = ((ctx.message.content).split(" "))[2]
    add_img(load_data(),item,url_image)

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

bot.run(TOKEN_DISCORD)
