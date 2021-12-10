import os
my_secret = os.environ['Token']
import discord
from discord.ext import commands
import flask
from flask import Flask
import threading
from threading import Thread

rule = commands.Bot(command_prefix='rule ', description="This is a ruler Bot")

 
@rule.command(brief="rules")
async def pls(ctx): 
    with open('pls', 'r') as f: #if you have the file in another folder use the path instead of just the name
        msg = f.read()
        await ctx.send(embed=discord.Embed(description=msg))

@rule.command
async def on_message(self, message):
    if message.content.startswith('lol'):
        await self.send_message(message.channel, 'o shit waddup!')
  


@rule.command(brief="code")
async def howtheymadeyou(ctx): 
    with open('howtheymadeyou', 'r') as f: #if you have the file in another folder use the path instead of just the name
        msg = f.read()
        await ctx.send(embed=discord.Embed(description=msg))
        

@rule.command() 
async def whichlanguagetheyusetomakeyou(ctx):
  await ctx.send("they use easiest language named python but why are you asking")
  
@rule.command() 
async def bestrict(ctx):
  await ctx.send("what is the meaning of strict? **lol**")


@rule.event
async def on_ready():
    activity = discord.Game(name="in Coding World", type=1)
    await rule.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
        

app = Flask("ECom website", template_folder=".",static_folder="/",static_url_path="/")

@rule.command() 
async def ping(ctx):
  await ctx.send("pong")
  
@rule.command()  
async def fart(ctx):
  await ctx.send ('only bot can fart in this server if other will fo be banned')
  
  
@rule.command(brief="Rules")
async def hl(ctx): 
    with open('hl', 'r') as f: #if you have the file in another folder use the path instead of just the name
        msg = f.read()
        await ctx.send(embed=discord.Embed(description=msg))
        
@rule.command(brief="Rules")
async def hlformat(ctx): 
    await ctx.send(file=discord.File('1628932686551.jpg'))
  
Thread(target=app.run,args=("0.0.0.0",8080)).start()
  
rule.run(my_secret)   
