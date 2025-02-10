import discord
from discord import app_commands
import aiohttp
import os

TOKEN = "place.token.here"  # Replace with your bot token
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()  # Sync commands globally
    print(f'✅ Logged in as {bot.user}')

@tree.command(name="cat", description="get car")
async def cat(interaction: discord.Interaction):
    print("🐱 Cat requested (The Cat API)")
    await interaction.response.defer()

    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
            if resp.status == 200:
                data = await resp.json()
                cat_image_url = data[0]["url"]
                await interaction.followup.send(cat_image_url)
            else:
                await interaction.followup.send("🐱 Couldn't fetch a cat image, try again!")

@tree.command(name="fox", description="get random fox")
async def fox(interaction: discord.Interaction):
    print("🦊 Fox requested (RandomFox API)")
    await interaction.response.defer()

    async with aiohttp.ClientSession() as session:
        # Fetch a random fox image from the RandomFox API
        async with session.get("https://randomfox.ca/floof/") as resp:
            if resp.status == 200:
                data = await resp.json()
                fox_image_url = data["image"]
                await interaction.followup.send(fox_image_url)
            else:
                await interaction.followup.send("🦊 Couldn't fetch a fox image, try again!")

bot.run(TOKEN)
