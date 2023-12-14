import discord
import random
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def omikuzi(message):
    OMIKUJI = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']
    message = OMIKUJI[random.randrange(len(OMIKUJI))]
    return message
