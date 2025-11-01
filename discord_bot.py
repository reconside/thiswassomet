import discord
from discord import app_commands
import os
from flask import Flask
from threading import Thread

# Flask server to keep the bot alive on Replit
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

client = MyClient()
tree = app_commands.CommandTree(client)

@tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
    latency = round(client.latency * 1000)
    await interaction.response.send_message(f'🏓 Pong! Latency: {latency}ms')

# Keep the bot alive on Replit
keep_alive()

# Run the bot
TOKEN = os.environ['DISCORD_BOT_TOKEN']
client.run(TOKEN)
