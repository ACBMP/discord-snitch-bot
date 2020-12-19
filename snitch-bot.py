import discord
import datetime

with open("config", "r") as config:
    config = config.readlines()
    TOKEN = config[0]
    CHANNEL_ID = config[1]
    BOT_ID = config[2]
    profanity_db = config[3].replace("\n", "")
    strict_profanity_db = config[4].replace("\n", "")

profanity_db = profanity_db.replace("profanity_db = ", "")
strict_profanity_db = strict_profanity_db.replace("strict_profanity_db = ", "")
with open(profanity_db, "r") as profanity_db:
    profanity_db = profanity_db.read().split("\n")

with open(strict_profanity_db, "r") as strict_profanity_db:
    strict_profanity_db = strict_profanity_db.read().split("\n")

TOKEN = TOKEN.replace("TOKEN = ", "")
CHANNEL_ID = int(CHANNEL_ID.replace("CHANNEL_ID = ", ""))
BOT_ID = int(BOT_ID.replace("BOT_ID = ", ""))
LFG = ["@LFG - PC", "@LFG - PSN", "@LFG - Xbox", "@LFG - Nintendo"]
LFG_TIMES = 4 * [datetime.datetime.now()]

client = discord.Client()

@client.event
async def on_ready():
    print("Starting.")

@client.event
async def on_message(message):
    report_chan = client.get_channel(CHANNEL_ID)

    async def check(db, strict=False):
        for word in db:
            if word in message.content.lower():
                msg = message.content
                user = message.author
                channel = message.channel
                await report_chan.send(f"User {user} used word {word} in {channel}.")
                await channel.send(f"{user.mention}, your use of the word {word} has been reported.")
                if strict:
                    await message.delete()
                return 0
            return 1


    if message.author.id != BOT_ID:
        if await check(strict_profanity_db, strict=True):
            if await check(profanity_db):
                for i in range(len(LFG) - 1):
                    if LFG[i] in message.content:
                        now = datetime.datetime.now()
                        if now - LFG_TIMES[i] < datetime.timedelta(minutes=14):
                            await message.channel.send(f"{message.author.mention}, please only ping once every 15 minutes. This has been reported.")
                            await report_chan.send(f"User {message.author} used {LFG[i]} within 15 minutes of a previous ping.")
                            await message.delete()

client.run(TOKEN)
