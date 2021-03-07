import discord
import random
from bot.api import IGDBAPIClient

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if '!docs' == message.content.lower():
        introductory_message = ("At your service🤖\n"
        "In order to get a recommendation type '!game' in chat💬\n"
        "The scope for recommendation can be specified in the following manner:\n"
        "Rating above certain value: '!game rating={number from 0 to 100}'\n"
        "Something in particular: '!game search={e.g. \"sonic the hedgehog\"}'\n"
        "Surely, all of the aforementioned commands can be combined e.g. as below:\n"
        "'!game search=\"sonic\" rating=75'\n"
        "GL HF😎")
        await message.channel.send(introductory_message)
    
    if '!game' in message.content.lower():
        api_client = IGDBAPIClient()
        rand_int = random.randint(1,99999)
        if '!game' == message.content.lower():
            try:
                result = api_client.get('games', f'fields *; where id = {rand_int};')
                await message.channel.send("🔥" + result[0]["name"] + "🔥") 
            except:
                await message.channel.send("Oops, something went wrong! Please, try again😅") 
        else:
            condition = []
            search_str = ""
            categories = message.content.lower().split()
            categories.pop(0)
            for category in categories:
                key, value = category.split("=")
                if key == "rating":
                    condition.append(f" rating > {value} ")
                if key == "search":
                    search_str += f"search {value} ; "
            condition_str = search_str + 'fields *; where' + '&'.join(condition) + ";" if len(condition) > 0 else search_str + 'fields *;'
            try:
                result = api_client.get('games', f'{condition_str}')
                await message.channel.send("🔥" + random.choice(result)["name"] + "🔥")
            except:
                await message.channel.send("Oops, something went wrong! Please, try again😅") 