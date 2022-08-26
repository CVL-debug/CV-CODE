from ast import Delete
from email import message
from http import client, server
from multiprocessing.connection import Client
import numbers
from pyexpat.errors import messages
from unicodedata import name
import discord
import random                                       #Developed with Discord.py by 『CVL』#9689
from discord.ext import commands


client = commands.Bot(command_prefix="?",intents=discord.Intents.all()) #The prefix ?

#------------------------------------------------------------------------------------------------------------------------------------------------

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Visual Studio Bot'))  #Bot status and activity
    print('Le Bot et prêt')

#------------------------------------------------------------------------------------------------------------------------------------------------

@client.command()
async def clean(ctx, amount=10):
				await ctx.message.delete()              #Command to delete the last 10 messages with ?clean
				await ctx.channel.purge(limit=amount)

#---------------------------------------------------------------------------------------------------------

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):   #Kick serv command with ?kick
    await member.kick(reason=reason)

#---------------------------------------------------------------------------------------------------------

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):     #Command Ban of the serv with ?ban
    await member.ban(reason=reason)


#---------------------------------------------------------------------------------------------------------



@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel("The channel ID")          #Event that allows the Bot to say welcome
    await general_channel.send(content=f"Welcome to  server name| {member.display_name}")



#---------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------

client.run("MTAxMjQ4NjIyMDA0MDkxMjk3Nw.G8kxAU.j6-LEbMZW56Ng5AvlB8m_KnfCh-AdL66-IuHro")
