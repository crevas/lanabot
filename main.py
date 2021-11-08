import discord

client = discord.Client()

COMMAND_PREFIX_kk = "라나야"
COMMAND_PREFIX_ke = "fkskdi"

@client.event
async def on_ready(self):
  print('Ready')
  await client.change_presence(game=discord.Game(name='다시 태어나려고', type=1))

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
