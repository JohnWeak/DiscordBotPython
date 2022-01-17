# bot.py
import discord
import random

TOKEN = "OTMwMTA3MzE0NjM0MTEzMDU1.YdxD8A.IXDdudKxLLex9MPKyvtK1MeaG6g"

client = discord.Client()


@client.event
async def on_ready():
	print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	channel = str(message.channel.name)
	user_message = str(message.content.lower())  # messaggio in lower case
	msg = str(message.content)  # messaggio così com'è stato inviato
	username = str(message.author).split("#")[0]
	print(f"<{username}> {user_message} -> ({channel})")

	if user_message == "!coinflip" or user_message == "!cf":
		risultato = random.randint(0, 1)
		if risultato == 0:
			testa_o_croce = "testa"
		else:
			testa_o_croce = "croce"
		await message.channel.send(f"È uscito {testa_o_croce}!")
		return

	if user_message == "hi bot":
		await message.channel.send("Hi human!")


client.run(TOKEN)
