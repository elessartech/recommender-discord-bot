import os
from dotenv import load_dotenv
from bot.bot import client 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == "__main__":
    client.run(TOKEN)