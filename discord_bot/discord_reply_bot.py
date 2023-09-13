import discord

from env._secrete import discord_notify_Token

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(f'on_message: {message}')
    if message.author == client.user:
        print("self message")
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$help'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ping'):
        await message.channel.send('pong')

    if message.content.startswith('$sync'):
        await message.channel.send('sync')
    if message.content.startswith('wow'):
        await message.channel.send('hoh')


client.run(discord_notify_Token)
