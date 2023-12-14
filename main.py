import discord
from datetime import datetime, timedelta
from discord.ext import commands
import dice, lucky, monitor

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
time_Count = {}

#サーバー起動確認
@client.event
async def on_ready():
    print('Botを起動しました。')

#ボイスチャット入退室確認
@client.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    if guild.id == 1134315592413872268:
        now = datetime.now()
        alert = guild.get_channel(1135258487472017478)
        if before.channel is None:
            message = f'{now:%m%d-%H:%M} に {member.name} が {after.channel.name} に参加しました'
            await alert.send(message)
            time_Count[member.id] = now
        elif after.channel is None:
            message = f'{now:%m%d-%H:%M} に {member.name} が {before.channel.name} を退出しました'
            await alert.send(message)
            exit_Time = now - time_Count[member.id]
            message = f'{member.name}は{monitor.format_timedelta(exit_Time)}いました'
            await alert.send(message)


@client.event
async def on_message(message):
    #ダイス
    msg = message.content
    result = dice.nDn(msg)
    if result is not None:
        await message.channel.send(result)

    #おみくじ
    if message.content == '/kuzi':
        omikuzi = lucky.omikuzi(message)
        await message.channel.send(f'あなたの運勢は"{omikuzi}"')


client.run('My TOKEN')