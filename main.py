import discord
import os
import random

client = discord.Client()

COMMAND_PREFIX_kk = "라나야"
COMMAND_PREFIX_ke = "fkskdi"

@client.event
async def on_ready():
  print('Ready')
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name="새롭게 태어나려고"))

@client.event
async def on_message():
  if str(message.channel.type) == "text":
    if message.content == "테스트":
      await message.channel.send("테스트 중입니다!")
    if message.content == "라나야" or message.content == "fkskdi":
      rm = random.randint(1, 4)
      if rm == 1:
        await message.channel.send("네?")
      if rm == 2:
        await message.channel.send("왜요?")
      if rm == 3:
        await message.channel.send("저요?")
      if rm == 4:
        await message.channel.send("저랑 놀아주세요!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
