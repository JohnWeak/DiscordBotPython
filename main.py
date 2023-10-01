# bot.py
import discord
from commands import do_stuff

TOKEN = open("token.txt").readline()

client = discord.Client()


@client.event
async def on_ready():
	print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
	if message.author == client.user:  # se è il messaggio di un bot, ignoralo
		return

	await do_stuff(message)


client.run(TOKEN)  # attiva il bot
