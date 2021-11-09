import discord
import os
import random
import json
import sqlite3

# DB 생성
#con = sqlite3.connect("memory.db")
# 커서 획득
#cur = con.cursor()
#예제 sql문
#sql1="CREATE TABLE ark(Id text,name text);"
#sql2="INSERT INTO ark Values('gain_time@naver.com','myblog4');"
#sql3="INSERT INTO ark Values('gain_time@naver.com','myblog4');"
#sql4="INSERT INTO ark Values('gain_time@naver.com','myblog4');"
#sql5="INSERT INTO ark Values('123123@naver.com','myblog4');"
#sql6="INSERT INTO ark Values('444241@naver.com','myblog4');"
#sql실행.
#cur.execute(sql1)
#cur.execute(sql2)
#cur.execute(sql3)
#cur.execute(sql4)
#cur.execute(sql5)
#cur.execute(sql6)
#commit
#con.commit()
#데이터 확인해보기.
#cur.execute('SELECT * FROM ark')
#for row in cur:
#  print(row)
#db연결해제.
#con.close()

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
        embed.set_footer(text="made by crevas")
        await message.channel.send(embed=embed)
      if message.content.split(" ")[1] == "배워":
        con = sqlite3.connect("memory.db")
        cur = con.cursor()
        sql1="CREATE TABLE ark(in text,out text);"
        sql2="INSERT INTO ark Values(message.content.split(" ")[2], message.content.split(" ")[3]);"
        cur.execute(sql1)
        cur.execute(sql2)
        con.commit()
        cur.execute('SELECT * FROM ark')
        for row in cur:
          await message.channel.send(row)
      
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
