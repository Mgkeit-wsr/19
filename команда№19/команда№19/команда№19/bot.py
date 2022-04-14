import discord 
from discord.ext import commands
from discord.ext.commands import Bot
from discord_components import *
import random
import time

#BD
summer1 = "Предлагаю посетить кинотеатр под открытым небом "
summer2 = "Чтобы насладиться захватывающшим видом отправляйтесь на крышу Мультимедия Арт Музея"
summer3 = "Вы можете выбраться на пикник или же на шашлыки, чтобы насладиться благоуханием природы"
winter1 = "Одна из лучших забав зимой - играть в снежки со своими друзьями!"
winter2 = "Лепите больших снеговиков и выкладывайте их в интернет, пусть ваши близкие оценят"
winter3 = "Зовите всех своих близких, чтобы провести прекрасное время за катанием на лыжах!"
spring1 = "Предлагаю прогуляться по набережной в парке или другом живописном месте"
spring2 = "Прогулки на лодке в парках, мимо старинных осабняков и храмов"
spring3 = "У вас есть возможность полюбоваться первыми листочками на деревьях, запечатлить появление первых подснежников, прекрасных трав и цветов"
autumm1 = "Предалагаю вам остаться у себя дома в тепле и уюте, пока за окнами идет сильный,проливной дождь. Почитайте свой любимый роман за кружечкой горячего чая"
autumm2 = "Вы можете замечательно провести время, пригласив к себе своих друзей"


k = random.randint(1,3)

bot = commands.Bot(command_prefix='!', help_command = None, intents = discord.Intents.all())

@bot.event 
async def on_ready():
    DiscordComponents(bot)
    print('Успешно запущен!')

@bot.command()
async def info(ctx):
	color = discord.Color(value = int('ff5c9a', 16))
	embed = discord.Embed(title = "Информация о проекте", description = "Для начала работы введите !start", color = color)
	await ctx.send(embed = embed)

@bot.command()
async def start(ctx):
	color = discord.Color(value = int('ff5c9a', 16))
	embed = discord.Embed(title = "Организация досуговой деятельности", description = "Выберите время года", color = color)
	msg = await ctx.send(embed = embed, components = [
                Button(style = ButtonStyle.blue, label = 'Зима'),  
                Button(style = ButtonStyle.green, label = 'Весна'),
                Button(style = ButtonStyle.grey, label = 'Осень'),
                Button(style = ButtonStyle.red, label = 'Лето') ])
	while True:
		responce = await bot.wait_for('button_click')
		if responce.message == msg:
			if responce.author == ctx.message.author:
				"""Блок лета"""
				if responce.component.label == 'Лето':
					color = discord.Color(value = int('52fc03', 16))
					embed = discord.Embed(color = color, title = "Лето", description = "Лето - это отличное время, которое позволит вам посетить большое количество уникальных мест")
					await ctx.send(embed = embed)					
					if k ==1:
						await ctx.send(f"{summer1}")
					elif k ==2:
						await ctx.send(f"{summer2}")
					else:
						await ctx.send(f"{summer3}")
				"""блок осени"""	
				if responce.component.label == 'Осень':
					color = discord.Color(value = int('fc5e03', 16))
					embed = discord.Embed(color = color, title = "Осень", description = "Осень неплохая пора, она добрая наоборот. А холодная специально, чтобы люди больше обнимались, чтобы согреться")
					await ctx.send(embed = embed)
					if k ==1:
						await ctx.send(f"{autumm1}")
					else:
						await ctx.send(f"{autumm2}")
				"""блок весны"""
				if responce.component.label == 'Весна':
					color = discord.Color(value = int('f803fc', 16))
					embed = discord.Embed(color = color, title = "Весна", description = "Весна похожа на мою лучшую подругу.\n Она тоже вечно опаздывает.")
					await ctx.send(embed = embed)
					if k ==1:
						await ctx.send(f"{spring1}")
					elif k ==2:
						await ctx.send(f"{spring2}")
					else:
						await ctx.send(f"{spring3}")
				"""юлок зимы"""
				if responce.component.label == 'Зима':
					color = discord.Color(value = int('839cf7', 16))
					embed = discord.Embed(color = color, title = "Зима", description = "Зима пробуждает аппетит. Пока на улицах лежит снег, шоколадное пирожное — лучшее лекарство")
					await ctx.send(embed = embed)
					if k ==1:
						await ctx.send(f"{winter1}")
					elif k ==2:
						await ctx.send(f"{winter2}")
					else:
						await ctx.send(f"{winter3}")



bot.run("OTY0MTA2NTA0NDczMDUxMTQ2.Ylf0Jg.XO6Da_zQDmLzk4Mk7PMXKqh11yw")