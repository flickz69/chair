from discord.ext import commands
import discord
import random as randm
import json
import os
import datetime
from Json.jsonhelper import jsonhelper


intents = discord.Intents.default()
intents.message_content = True

chair = discord.ext.commands.Bot(command_prefix = "chair::", intents=intents)

blacklisted = jsonhelper.getvar("config.json", "blacklisted")
testmode = jsonhelper.getvar("config.json","testmode")

print(r"""       _           _      
      | |         (_)     
   ___| |__   __ _ _ _ __ 
  / __| '_ \ / _` | | '__|
 | (__| | | | (_| | | |   
  \___|_| |_|\__,_|_|_|   
                          
                          
                          """)

@chair.event
async def on_ready():
     await chair.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"NULLS FOR IOS DOESNT EXIST | chair::help"))
      
@chair.remove_command('help')

@chair.command()
async def help(ctx):
    await ctx.author.send(jsonhelper.getvar("tids.json", "v1"))

@chair.command()
async def random(ctx, arg):
    if ctx.author.id in blacklisted:
      await ctx.send("your a skid bro🙄")
    else:
       var = randm.randint(0, 100)
       await ctx.send(f'{arg} is {var}% wheelchaired')
       
@chair.command()
async def me(ctx):
     rd = randm.randint(0, 100)
     await ctx.send(f'i am {rd}% wheelchaired')
     if 80 <= rd <= 90:
       await ctx.author.send(jsonhelper.getvar("tids.json", "v2"))
       
@chair.command()
async def setstatus(ctx, *, a1: str):
     isdev = jsonhelper.getvar("config.json","devs")
     if ctx.author.id not in isdev:
       await ctx.send("sob")
     else:
          await chair.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{a1}"))
          await ctx.author.send(f"successfully changed status to {a1}")
          
@chair.command()
async def qrand(ctx):
     getquotenum = jsonhelper.getvar("quotes.json","rand")
     num = randm.randint(0,getquotenum)
     quotes = jsonhelper.getvar("quotes.json",f"{num}")
     await ctx.send(f"{quotes}")
    
      

if testmode == True:
  chair.run('')
else:
     chair.run('')