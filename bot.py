import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
# import random
import funny
import lyricwikia
import asyncio
import youtube_dl
from discord.voice_client import VoiceClient
from ffmpeg import *
from discord import FFmpegPCMAudio
from discord.utils import get

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
def randomMessage():
    word = ['Animal', 'Dog', 'Cat', 'Queen', 'Bird']
    return ' '.join(random.sample(word, 1))
def main():
    client = discord.Client()
    bot = commands.Bot(command_prefix='.')
    @client.event
    async def on_ready():
        for guild in client.guilds:
            # if guild.name == GUILD:
            #     break

            print(
                f'{client.user} is connected to follwing server: \n'
                f'{guild.name}(id: {guild.id}) Totle Members: {guild.member_count} \n'
                )
            print (client.guilds)
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Guild Members:\n - {members}')
    @client.event
    async def on_message(message):
        if '.funny' in message.content.lower():
            await message.channel.send(funny.printstr())
        elif '.hello' in message.content.lower():
            await message.channel.send("Hello Human")
    @bot.command()
    async def lyric(ctx, *, arg):
        await ctx.send(lyricwikia.get_lyrics(arg))
    @asyncio.coroutine


    @bot.command()
    async def play(ctx, arg1):
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            source = FFmpegPCMAudio(arg1)
            player = voice.play(source)
    bot.run(TOKEN)
    client.run(TOKEN)

if __name__ == "__main__":
    main()