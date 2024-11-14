import discord
import asyncio

from dotenv import load_dotenv

from courses import Course
from datetime import datetime

import os


load_dotenv()


def getToken():
    # code to open and read token
    return os.environ.get("TOKEN")


token = get_token()

from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"), intents=intents)


def fetch_course(crn: str) -> str:
    season = "spring"
    now = datetime.now()
    term = ""

    if season.lower() == "spring":
        term = f"{now.year + 1}" + "02" if now.month > 4 else f"{now.year}" + "02"
    else:
        term = (
            f"{now.year}" + "05" if season.lower() == "summer" else f"{now.year}" + "08"
        )
    course = Course(crn, term)
    return str(course)


@bot.command()
async def info(ctx, crn):
    await ctx.send(fetch_course(crn))


@bot.command()
async def ping(ctx):
    print(ctx)
    await ctx.send(f"Pong! {round(bot.latency * 1000)} ms")


bot.run(getToken())
