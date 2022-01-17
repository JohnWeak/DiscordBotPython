# commands.py
# Lista di comandi che il bot dovrà eseguire
import random


async def do_stuff(message):
	channel = str(message.channel.name)
	user_message = str(message.content.lower())  # messaggio in lower case
	msg = str(message.content)  # messaggio così com'è stato inviato
	username = str(message.author).split("#")[0]
	print(f"<{username}> {user_message} -> ({channel})")

	if user_message == "!coinflip" or user_message == "!cf":
		await coinflip(message)

	if user_message.find("!8ball") != -1:
		await eight_ball(message)


async def coinflip(message):
	risultato = random.randint(0, 1)
	if risultato == 0:
		testa_o_croce = "testa"
	else:
		testa_o_croce = "croce"
	await message.channel.send(f"È uscito {testa_o_croce}!")
	return


async def eight_ball(message):

	file = open("risposte_it.txt", "r")
	lines = file.readlines()
	risultato = random.randint(0, len(lines))
	risposta = ""
	for i in range(risultato):
		lines[i].replace("\n", "")
		risposta = lines[i]

	await message.channel.send(risposta)
	return
