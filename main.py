import discord
import os
import random

client = discord.Client()

command_prefix = "라나야"

@client.event
async def on_ready():
  print('Ready')
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name="새로운 라나가 되려고"))

@client.event
async def on_message(message):
  if message.content == "테스트":
    await message.channel.send("정상 작동 중!")
  if message.content == "라나야":
    rm = random.randint(1, 4)
    if rm == 1:
      await message.channel.send("네?")
    if rm == 2:
      await message.channel.send("왜요?")
    if rm == 3:
      await message.channel.send("저요?")
    if rm == 4:
      await message.channel.send("저랑 놀아주세요!")
  if message.content.split(" ")[0] == command_prefix:
    if message.author.bot == 0:
      # Command ( if message.content.split(" ")[1] == "Command Name" )
      if message.content.split(" ")[1] == "초대":
        embed = discord.Embed(title="[봇] 라나", description="저랑 놀아주세요!", color=0x0FF1CE)
        embed.add_field(name="라나와 놀고 싶다면 링크 클릭!", value=":link: https://discord.com/api/oauth2/authorize?client_id=841739951040888844&permissions=8&scope=bot", inline=False)
        embed.set_footer(text="made by crevas",image_url='https://cdn.discordapp.com/attachments/907481613913436180/907481813591662592/130_20210809091743.png')
        await message.channel.send(embed=embed)
      
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
