# Game Recommender Discord Bot

## Description

A discord bot, written in Python, that recommends random games to play according to the provided parameters. Uses [IGDB API](https://www.igdb.com/api).


## Environment 

| Avainsana |
| ------ | 
| DISCORD_TOKEN  | 
| DISCORD_GUILD |  
| IGDB_API_TOKEN |  
| IGDB_API_USER_ID |  
| TWITCH_API_TOKEN | 

## Launch

- Install required packages:
```
pip install -r requirements.txt
```
- Run the bot:
```
python main.py
```

## Functionality

The bot can be controlled via messages to the discord server.

- Show full documentation: `!docs`.
- Search game with rating above certain value: `!game rating={number from 0 to 100}`
- Search game that should contain a string in the title: `!game search={e.g. "sonic the hedgehog"}`
- Search game that combines aforementioned parameters: `!game search="sonic" rating=75`
