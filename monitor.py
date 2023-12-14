# This example requires the 'members' and 'message_content' privileged intents to function.
import discord
from discord.ext import commands
from datetime import datetime, timedelta

intents = discord.Intents.default()
client = discord.Client(intents = intents)
time_Count = {}

def format_timedelta(timedelta):
  total_sec = timedelta.total_seconds()
  # hours
  hours = total_sec // 3600
  # remaining seconds
  remain = total_sec - (hours * 3600)
  # minutes
  minutes = remain // 60
  # remaining seconds
  seconds = remain - (minutes * 60)
  # total time
  return '{:02}時間{:02}分{:02}秒'.format(int(hours), int(minutes), int(seconds))
