import discord
import sys
from discord.ext import commands

TOKEN = (sys.argv[1])#Токен бота
bot = commands.Bot(command_prefix='!')#Префикс бота '!'

@bot.command(pass_context=True) #Разрешение на передачу аргументов
async def test(ctx, arg): #Асинхронная функция бота
	await ctx.send(arg) #отправляем обратно аргумент

bot.run(TOKEN)