'''
For setting up your discord bot on the server,
Visit : https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

Any update make a pull request and if you like this project give a star ⭐
'''

import discord
from src.main import CodinAPI

client = discord.Client()
user = CodinAPI()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # add your email and password
    await user.login('YOUR_EMAIL', 'YOUR_PASSWORD')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Use clash command to create a clash
    if message.content.startswith('$clash'):
        await user.create_clash()
        await message.channel.send(user.get_clash_url())


# add your bot token here
client.run('YOUR_DISCORD_BOT_API_TOKEN')
