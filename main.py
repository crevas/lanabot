'''
    <main.py>
    디스코드 봇의 메인이 되는 파일입니다. 이 파일을 실행해야 디스코드 봇을 실행할 수 있어요!
    ※ 봇 개발 초심자라면 이 파일을 수정하지 않는 것을 추천드려요!
    - 키뮤 제작(0127 버전)
'''

from discord.ext import commands
import discord

import random
from config import Config
from utils import logger
import re
import os


class SetaBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=Config.prefixes,  # 접두사는 config.py에서 설정
            help_command=None,
        )

        # Cogs 로드(Cogs 폴더 안에 있는 것이라면 자동으로 인식합니다)
        cog_list = [i.split('.')[0] for i in os.listdir('cogs') if '.py' in i]
        cog_list.remove('__init__')
        self.add_cog(AdminCog(self))  # 기본 제공 명령어 Cog
        for i in cog_list:
            self.load_extension(f"cogs.{i}")

    async def on_ready(self):  # 봇이 구동되면 실행
        logger.info('======================')
        logger.info('< 구동 완료 >')
        logger.info(f'봇 이름 : {self.user.name}')
        logger.info(f'봇 아이디 : {self.user.id}')
        logger.info('======================')

        await self.change_presence(
            status=discord.Status.online,  # 상태 설정
            activity=discord.Game(name=Config.activity))  # 하고 있는 게임으로 표시되는 것 설정
    
    async def on_message(self, message):
        if str(message.channel.type) == "text":
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
            if message.content.split(" ")[0] == command_prefix:
                if message.author.bot == 0:
                    if message.content.split(" ")[1] == "초대":
                        embed = discord.Embed(title=[봇] 라나, description="저랑 놀아주세요!", color=0x00E0FF)
                        embed.add_field(name="라나와 놀고 싶다면 아래 링크 클릭!", value=":link: https://discord.com/api/oauth2/authorize?client_id=841739951040888844&permissions=8&scope=bot", inline=False)
                        await message.channel.send(embed=embed)
                    if message.content.split(" ")[1] == "테스트":
                        await message.channel.send("테스트 중이에요!")

    def run(self):
        super().run(Config().using_token(), reconnect=True)


# 기본 제공 명령어
class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # cogs 폴더 안의 코드를 수정했다면 굳이 껐다 키지 않아도 다시시작 명령어로 적용이 가능해!
    @commands.command()
    async def 다시시작(self, ctx, *args):
        if ctx.author.id not in Config.admin:
            await ctx.send('권한이 부족해요!\n`라나 관리자라면 config.py의 admin 리스트에 디스코드 id가 있는지 확인해 보세요!`')
            return None

        w = await ctx.send("```모듈을 다시 불러오는 중...```")
        cog_list = [i.split('.')[0] for i in os.listdir('cogs') if '.py' in i]
        cog_list.remove('__init__')
        for i in cog_list:
            self.bot.reload_extension(f"cogs.{i}")
            logger.info(f"'{i}' 다시 불러옴")

        await w.edit(content="```cs\n'불러오기 성공'```")
       async def 


setabot = SetaBot()
setabot.run()
