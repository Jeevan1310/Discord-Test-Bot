import discord
from discord import channel
from discord import guild
from discord import user
from discord.ext import commands

client=commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Defence master'))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  channel=message.channel
  if message.author == client.user:
    return
  msg = message.content
  if message.content.startswith('hello'):
    await message.channel.send(f'Hello! {message.author.mention} ')
  if message.content.startswith('block me'):
    await message.channel.send(f'You were blocked by admin {message.author.mention}')
  if message.content.startswith('Thank you'):
    await message.add_reaction('\U0001F60A')
  
  if message.content.startswith('!role'):
    role_to_assign = message.content.split(" ")[1]
    print(role_to_assign, type(role_to_assign))
    await message.guild.create_role(name=role_to_assign)
    var = discord.utils.get(message.guild.roles, name=role_to_assign)
    await message.author.add_roles(var)
    await channel.send(f"<{message.author.mention}> has been assigned the role <{role_to_assign}>")
  
  if message.content.startswith('!give'):
    await message.send('Enter user id to whom you want to assign role')
    user_id_no = message.content.split(" ")[1]
    await message.send('Enter role')
    role_to_assign=message.content.split(" ")[2]



    


@client.event
async def on_member_join(member):
  guild = client.get_guild(927554077959786558)
  channel = guild.get_channel(928717528933486684)
  await channel.send(f'Welcome to the server {member.mention}  :tada:')
  await member.send(f'welcome to {guild.name}  , {member.name}  :tada:')

@client.event
async def on_reaction_add(reaction,user):
  reaction_channel = client.get_channel(928717579118334093)
  await reaction_channel.send(f'{user.name} gave reaction to {reaction.message.author} with {reaction.emoji}')

@client.command()
async def ping(ctx):
    await ctx.send('pong!')




client.run('token number')