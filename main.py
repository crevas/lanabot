import discord
import os
import random
import json

client = discord.Client()

command_prefix = "라나야"

@client.event
async def on_ready():
  print('Ready')
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name="새로운 라나가 되려고"))

@client.event
async def on_message(message):
  if message.content.split(" ")[0] != command_prefix:
    with open('memory.json', 'r') as f:
      json_data = json.load(f)
      message = str(message.content.split(" ")[0])
      send = json_data['str'][f'{message}']
      await message.channel.send(str(send))
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
        embed.set_footer(text="made by crevas")
        await message.channel.send(embed=embed)
      if message.content.split(" ")[1] == "배워":
        input = message.content.split(" ")[2]
        output = message.content.split(" ")[3]
        if input == None or output == None:
          return False
        elif input == None and output == None:
          return False
        else:
          with open('memory.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data['str']:
              if str(input) in i:
                embed = discord.Embed(title=f"{input}은(는) 이미 알고있는 단어에요!", description="가르칠 수 없어요!", color=0x0FF1CE)
                await message.channel.send(embed=embed)
                return False
          data['str'][f'{input}'] = str(output)
          with open('memory.json', 'w', encoding='utf-8') as ff:
            json.dump(data, ff, ensure_ascii=False, indent='\t')
          
          embed = discord.Embed(title=f"{input}은(는) {output}이군요?", description="기억해둘게요!", color=0x0FF1CE)
          await message.channel.send(embed=embed)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
