# commands.py
# Lista di comandi che il bot dovrà eseguire
import random
import discord


async def do_stuff(message):
	channel = message.channel
	channel_name = str(message.channel.name)
	user_message = str(message.content.lower())  # messaggio in lower case
	msg = str(message.content)  # messaggio così com'è stato inviato
	username = str(message.author).split("#")[0]
	client = discord.Client()
	print(f"{username}: \"{user_message}\" in #{channel_name} ")

	if user_message == "!coinflip" or user_message == "!cf":
		await coinflip(message)

	if "!8ball" in user_message:
		await eight_ball(channel)

	if "test" in user_message:
		await test(message)

# fine do_stuff()


async def coinflip(message):
	risultato = random.randint(0, 1)
	toc = ["testa", "croce"]
	await message.channel.send(f"È uscito {toc[risultato]}!")
	return

# fine coinflip()


async def eight_ball(channel):

	file = open("risposte_it.txt", "r")
	lines = file.readlines()
	risultato = random.randint(0, len(lines))
	risposta = ""
	for i in range(risultato):
		lines[i].replace("\n", "")
		risposta = lines[i]

	await channel.send(f":8ball: dice... **{risposta}**", mention_author=True)
	return

# fine eight_ball()


async def test(message):
	await message.add_reaction("🎱")
	return

# fine test()


