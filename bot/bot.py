import discord
import random
from bot.api import IGDBAPIClient

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '!docs' == message.content.lower():
        introductory_message = "At your service🤖\nIn order to get a recommendation for a game to play type '!game' in chat💬👇"
        await message.channel.send(introductory_message)
    
    if '!game' == message.content.lower():
        api_client = IGDBAPIClient()
        rand_int = random.randint(1,99999)
        result = api_client.get('games', f'fields *; where id = {rand_int};')
        print(result[0])
        await message.channel.send(result[0]["name"])