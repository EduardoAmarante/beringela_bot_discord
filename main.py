import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def clear(ctx, amount=0):

    print(amount)
    if ctx.author.guild_permissions.administrator:
        if amount > 0:
            print(amount,' valor do amount')
            await ctx.channel.purge(limit=amount)
            sucess = await ctx.send (f"{amount} messages has been deleted") #sending success msg
            
            await sucess.delete()
        else:
            await ctx.send("You need to enter a number higher than 0")
    else:
        await ctx.send("You need to be an admin to use this command")

@bot.command()
async def linkedin(ctx,content):
    
    print(ctx.author.name)
    embed = discord.Embed(
        title=ctx.author.name,
        url=content,
        description="[Acesse]({}) {}'s linkedin".format(content,ctx.author.name),
        color=discord.Color.blue(),
        
        )
    embed.set_thumbnail(url=ctx.author.display_avatar) 
    await ctx.channel.purge(limit=1)

    await ctx.send(embed=embed)


bot.run('token')
