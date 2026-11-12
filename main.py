import os import discord
from discord.ext import commands
intents = discord.Intents.default)
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!",
intents=intents)
@bot.event
async def on_ready(:
ا تم تسجيل الدخول بنجاح باسم"
@bot.command()
async def ping(ctx):
!البوت شغال وزي الفل يا طويل العمر")await ctx.send
("
bot.run(os.getenv("TOKEN"))
