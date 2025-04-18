import asyncio
import os
import random

from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')


@bot.event
async def on_member_join():
    print(f'Hello suck my dick {bot.user.name}!')


@bot.command()
async def trollmove(ctx, member: discord.Member):
    if member.voice is None:
        await ctx.send(f"{member.display_name} не в голосовому каналі!")
        return

    voice_channels = [vc for vc in ctx.guild.voice_channels if vc.permissions_for(member).connect]

    if len(voice_channels) < 2:
        await ctx.send("Потрібно хоча б 2 голосові канали для переміщення.")
        return

    await ctx.send(f"😈 Починаю тролити {member.display_name}...")

    for i in range(20):
        random_channel = random.choice(voice_channels)
        try:
            await member.move_to(random_channel)
            print(f"👉 Перекинув у {random_channel.name}")
            await asyncio.sleep(0.5)
        except Exception as e:
            await ctx.send(f"❌ Помилка при переміщенні: {str(e)}")
            break

    await ctx.send("🎉 Тролінг завершено!")


@bot.command()
async def hello(ctx):
    await ctx.send('Hello there! 👋')


bot.run(TOKEN)
