import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()
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
client.run(TOKEN)