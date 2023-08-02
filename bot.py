import discord
import requests
from bs4 import BeautifulSoup
import random
import os

# Set up client
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.default())

# Function to perform web scraping and get data from 5e.tools
def get_table_data():
    url = 'https://example.com/dnd-table-url'  # Replace with the actual URL of the table you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract and parse the relevant table data here
    # ...

# Command to roll on a D&D 5e table
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!roll'):
        table_data = ['hello','random','wow']
        # Perform the rolling logic using the data obtained
        result = random.choice(table_data)
        await message.channel.send(f'You rolled: {result}')

client.run(TOKEN)
