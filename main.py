import discord
import json
import os
import asyncio
import random

with open('bot/token.txt', 'r') as f:
  TOKEN = f.read()

INTENTS = nextcord.Intents.default()
INTENTS.members = True

client = nextcord.Client()

COMMAND_PREFIX_kk = "라나야"
COMMAND_PREFIX_ke = "fkskdi"

class MyClient(nextcord.Client):
  # Bot Ready Event
  async def on_ready(self):
    print('Ready')
    try:
      while True:
        guilds = int(0)
        for i in client.guilds:
          guilds += 1
        await self.change_presence(status=nextcord.Status.online, activity=nextcord.Game(f"라나야 도와줘 │ 여러 서버들을 구경"))
        try:
          for i in client.guilds:
            path = f"guilds/{i.id}"
            if os.path.isdir(path):
              dummy = ""
            else:
              os.mkdir(f"guilds/{i.id}")
              with open(f"guilds/{i.id}/config.json", "a") as f:
                with open("bot/config.json", "r") as r_f:
                  print(r_f.read(), file=f)
          await asyncio.sleep(2)
        except:
          print("EventError: on_ready")
    except:
      print("EventError: on_ready")

    # Message Send Event
  async def on_message(self, message):
    if str(message.channel.type) == "text":
      # Commands
      if message.content == "라나야":
        rm = random.randint(1, 4)
        if rm == 1:
          await message.channel.send("네?")
        if rm == 2:
          await message.channel.send("저요?")
        if rm == 3:
          await message.channel.send("왜요?")
        if rm == 4:
          await message.channel.send("놀아주세요!")
      if message.content.split(" ")[0] == COMMAND_PREFIX_kk or message.content.split(" ")[0] == COMMAND_PREFIX_ke:
        if message.author.bot == 0:
          # Command ( if message.content.split(" ")[1] == "Command Name" )
          if message.content.split(" ")[1] == "홍보":
            embed = nextcord.Embed(title="FLANA", description="거대한 RPG", color=0xDAF7A6)
            embed.add_field(name="**세상은 넓고 아름다워!**", value="10000 10000 크기의 거대한 오픈월드!\n총 6개의 대륙과 대륙마다 수많은 던전들!\n던전마다 다른 몬스터들과 던전 어딘가에 숨겨진 히든퀘스트!", inline=False)
            embed.add_field(name="**너는 어떤 사람일까?**", value="10개의 기본 클래스와 숨겨진 히든 클래스들!\n각 클래스마다 다른 여러 스킬들!\n도장에서 전투스타일을 습득하여 남들과는 다르게!", inline=False)
            embed.add_field(name="**때론 혼자보단 여럿이 좋을거야!**", value="길드에 가입해서 여러 사람들과 함께 즐겨봐!\n길드에 가입하면 길드 특성에 따라 다른 패시브?\n전쟁, 레이드 등 다양한 길드 컨텐츠!", inline=False)
            embed.add_field(name="**지쳤다면 쉬어도 괜찮아!**", value="여관에서 휴식하면서 체력 회복!\n농사, 요리, 연금술을 해도 똑같이 성장할 수 있어!", inline=False)
            await message.channel.send(embed=embed)
          if message.content.split(" ")[1] == "게임":
            if message.content.split(" ")[2] == "참가":
              if os.path.isdir(f"member/{message.author.id}"):
                await message.channel.send("이미 데이터가 남아있습니다")
              else:
                await message.channel.send("게임에 참여하셨습니다")
                os.mkdir(f"member/{message.author.id}")
                with open(f"member/{message.author.id}/config.json", "a") as f:
                  print('{\n  "user-name": ' + f'"{message.author.display_name}",' + '\n  "user-id": ' + f'"{message.author.id}",' + '\n  "money": ' + '10000' + '\n}', file=f)
            if message.content.split(" ")[2] == "정보":
              with open(f"member/{message.author.id}/config.json", "a") as file2:
                print("d")
          if message.content.split(" ")[1] == "타이머":
            await message.channel.send("타이머를 시작합니다")
            timer = int(message.content.split(" ")[2])
            await asyncio.sleep(timer)
            await message.channel.send(message.author.mention + "님! 타이머가 끝났습니다!")
          if message.content.split(" ")[1] == "가위바위보":
            embed = nextcord.Embed(title="가위바위보", description="선택해주세요", color=0xDAF7A6)
            msg = await message.channel.send(embed=embed)
            await msg.add_reaction("✌")
            await msg.add_reaction("✊")
            await msg.add_reaction("🖐")
          if message.content.split(" ")[1] == "뽑기":
            if message.channel.id == 897026792911675392:
              r1 = random.randint(1, 1000)
              if r1 == 1:
                await message.channel.send(f"`{message.author.display_name}`님! 당첨되었습니다!\n해당 사진을 찍어서 크래바스에게 보내주시면 확인 후, 5000 포인트를 드립니다!")
              else:
                await message.channel.send(f"`{message.author.display_name}`님.. 안타깝지만 당첨되지 않았습니다...")
            else:
              await message.channel.send("여기는 뽑기채널이 아닙니다")
          if message.content.split(" ")[1] == "잘했어":
            await message.channel.send("데헷^^ 감사합니당")
          if message.content.split(" ")[1] == "주사위":
            randomNum = random.randint(1, 6)
            if randomNum == 1:
              await message.channel.send(embed=nextcord.Embed(description=':game_die: '+ ':one:'))
            if randomNum == 2:
              await message.channel.send(embed=nextcord.Embed(description=':game_die: ' + ':two:'))
            if randomNum == 3:
              await message.channel.send(embed=nextcord.Embed(description=':game_die: ' + ':three:'))
            if randomNum == 4:
              await message.channel.send(embed=nextcord.Embed(description=':game_die: ' + ':four:'))
            if randomNum == 5:
              await message.channel.send(embed=nextcord.Embed(description=':game_die: ' + ':five:'))
            if randomNum == 6:
              await message.channel.send(embed=nextcord.Embed(description=':game_die: ' + ':six: '))
          if message.content.split(" ")[1] == "도와줘" or message.content.split(" ")[1] == "ehdhkwnj":
            try:
              with open("bot/help.txt",'r') as f:
                help = f.read()
              embed = nextcord.Embed(title="라나 도움말", description=help, color=0xDAF7A6)
              embed.add_field(name="출처", value="[초대하기](https://discord.com/api/oauth2/authorize?client_id=841739951040888844&permissions=8&scope=bot)\nmade by crevas", inline=False)
              await message.author.send(embed=embed)
              await message.channel.send(f"`{message.author.display_name}`님에게 명령어 리스트를 보냈습니다.")
            except:
              await message.reply(f"`{message.author.display_name}`님의 개인 메시지 받기 설정이 꺼져있습니다.")
          if message.content.split(" ")[1] == "버전" or message.content.split(" ")[1] == 'qjwjs':
            await message.channel.send("```css\n[ 개발언어 ] .Nextcord.py\n[ 현재버전 ] 0.0.1 beta\n[ 개발버전 ] 0.01 test\n```")


          if message.content.split(" ")[1] == "정보" or message.content.split(" ")[1] == "wjdqh":
            if message.author.guild_permissions.administrator is True:
              with open(f'guilds/{message.guild.id}/config.json', 'r') as f:
                data = f.read()
              data = data.replace(",", ",\n")
              await message.channel.send(f'```json\n{data}```')
            else:
              await message.reply("`관리자`권한이 없습니다.")


keep_alive()
client = MyClient(intents=INTENTS)
client.run(TOKEN)
