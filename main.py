import discord
import os

client = discord.Client()

COMMAND_PREFIX_kk = "라나야"
COMMAND_PREFIX_ke = "fkskdi"

@client.event
async def on_ready():
  print('Ready')
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name="새롭게 태어나려고"))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
