from operator import truediv
import discord
from discord.ext import commands
import os


from dotenv import load_dotenv
load_dotenv()
CLIENT_ID_TWITCH = os.getenv("CLIENT_ID_TWITCH")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
TOKEN_DISCORD = os.getenv("TOKEN_DISCORD")
TWITCH_SECRET = os.getenv("TWITCH_SECRET")

# CLIENT_ID_TWITCH = os.environ.get("CLIENT_ID_TWITCH")
# DISCORD_GUILD = os.environ.get("DISCORD_GUILD")
# TOKEN_DISCORD = os.environ.get("TOKEN_DISCORD")
# TWITCH_SECRET = os.environ.get("TWITCH_SECRET")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.dm_messages = True
intents.guild_messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('on ready')

# @bot.command()
# async def clear(ctx, amount=0):

#     print(amount)
#     if ctx.author.guild_permissions.administrator:
#         if amount > 0:
#             print(amount,' valor do amount')
#             await ctx.channel.purge(limit=amount)
#             sucess = await ctx.send (f"{amount} messages has been deleted <a:white_check_mark:>") #sending success msg
#             await asyncio.sleep(10)
#             await sucess.delete()
#         else:
#             await ctx.send("You need to enter a number higher than 0")
#     else:
#         await ctx.send("You need to be an admin to use this command")

@bot.event
async def on_message(message: discord.Message):
    if "gosto" in message.content:
        await message.channel.send(f'EU GOSTUUMMM!')

bot.run(TOKEN_DISCORD)
