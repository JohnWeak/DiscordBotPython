# bot.py
import discord
from commands import do_stuff

TOKEN = "OTMwMTA3MzE0NjM0MTEzMDU1.YdxD8A.IXDdudKxLLex9MPKyvtK1MeaG6g"

client = discord.Client()


@client.event
async def on_ready():
	print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	await do_stuff(message)


client.run(TOKEN)
