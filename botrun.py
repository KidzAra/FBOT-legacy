import discord
from discord.ext import commands
import os, sqlite3
import requests
import json

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Все работет')

    global base, cur
    base = sqlite3.connect('Бот.db')
    cur = base.cursor()
    if base:
        print('DataBase connected')


@bot.command()
async def version(ctx):
    await ctx.send('Версия Fbot 0.4 вы сейчас участвете в его тесте :) Нововведения: -Модерирование ')

@bot.command()
async def канава(ctx):
    await ctx.send('Кана́ва — открытая горная или геологоразведывательная выработка, имеющая небольшие по сравнению с длиной поперечные размеры. ')

@bot.command()
async def Повтори(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def повтори(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def watch(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 755600276941176913, # YouTube Together
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def Betrayal(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 773336526917861400, # Betrayal
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def Fishing(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 814288819477020702, # фишинг мамонтов
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def poker(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 755827207812677713, # покер
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def chess(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 832012774040141894, # шахматы
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def youtube(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 755600276941176913, # YouTube Together
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def letter(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 879863686565621790, # леттер
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def snake(ctx):

	data = {
		"max_age": 86400,
		"max_uses": 0,
		"target_application_id": 879863976006127627, # змейка вроде
		"target_type": 2,
		"temporary": False,
		"validate": None
	}
	headers = {
		"Authorization": "Bot ODc1MDY1MDEzNzcyMDkxNDMy.YRQFzQ.gryw40xFlmeh0oYcV_yFVfA5QDM",
		"Content-Type": "application/json"
	}

	if ctx.author.voice is not None:
		if ctx.author.voice.channel is not None:
			channel = ctx.author.voice.channel.id
		else:
			await ctx.send("Зайдите в канал")
	else:
		await ctx.send("Зайдите в канал")

	response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
	link = json.loads(response.content)

	await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def activity(ctx):
    emb = discord.Embed( title = 'activities' )
    emb.set_image( url = 'https://i.imgur.com/qgDiS6x.png' )
    await ctx.send( embed = emb )

@bot.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear(ctx):
	await ctx.channel.purge( limit = 10 )

@bot.command( pass_context = True )
@commands.has_permissions( kick_members = True)

async def kick( ctx, member: discord.Member, *, reason ):
	await ctx.channel.purge( limit = 1)

	await member.kick( reason = reason )

@bot.command( pass_context = True )
@commands.has_permissions( ban_members = True)

async def ban( ctx, member: discord.Member, *, reason ):
	await ctx.channel.purge( limit = 1)

	await member.ban( reason = reason )


bot.run(os.getenv('TOKEN'))
