import discord
from discord.ext import commands
client=commands.Bot(command_prefix='!')
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Defence master'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if message.content.startswith('hello'):
    await message.channel.send(f'Hello! {message.author.mention} ')
  if message.content.startswith('block me'):
    await message.channel.send(f'You were blocked by admin {message.author.mention}')
  if message.content.startswith('Thank you'):
    await message.add_reaction('\U0001F60A')

@client.event
async def on_member_join(member):
  guild = client.get_guild(927554077959786558)
  channel = guild.get_channel(928717528933486684)
  await channel.send(f'Welcome to the server {member.mention}  :tada:')
  await member.send(f'welcome to {guild.name}  , {member.name}  :tada:')

@client.command()
async def ping(ctx):
    await ctx.send('pong!')




client.run('OTI4NzEwODc1NjI2NDk2MDYw.YdcvZw.7ZV7RljXzBGoqJkS4RTrw4kMB-Y')