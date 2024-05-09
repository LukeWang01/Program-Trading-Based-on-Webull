import asyncio
import threading
import time
import discord
from discord.ext import commands
from env._secrete import discord_notify_Token, channel_id_general
from dotenv import load_dotenv
import os

load_dotenv()
discord_notify_Token = os.getenv('DISCORD_NOTIFY_TOKEN')
channel_id_general = os.getenv('CHANNEL_ID_GENERAL')


class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents, message, channel_id):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.on_ready_message = message
        self.channel_id = channel_id

        @self.command()
        @commands.has_permissions(administrator=True)
        async def sync_command(ctx):
            await self.tree.sync()
            await ctx.send("syncing...")

        @self.hybrid_command()
        async def say_hi(ctx, name: str):
            await ctx.send(f"Hi {name}!")

        @self.hybrid_command()
        async def ping(ctx):
            await ctx.send("pong pong")

    async def on_ready(self):
        channel = self.get_channel(self.channel_id)
        if channel:
            await channel.send(self.on_ready_message)
            print(f"Message sent to channel {self.channel_id}")

    async def close_bot(self):
        await self.close()


def send_notification(bot_obj):
    try:
        bot_obj.run(discord_notify_Token)
    # bot_obj.loop.run_forever()
    except Exception as e:
        pass
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot_obj.close_bot())
    loop.stop()  # Stop the event loop


def run_bot_send_msg_new_thread(msg, channel_id=channel_id_general):
    # print("start")
    command_prefix = "!"
    intents = discord.Intents.default()
    bot = MyBot(
        command_prefix=command_prefix,
        intents=intents,
        message=msg,
        channel_id=channel_id,
    )

    thread_bot = threading.Thread(target=send_notification, args=(bot,))
    thread_bot.start()
    # print('thread started')
    time.sleep(5)  # wait for bot to send msg before stopping
    # print('thread stopping')
    bot.loop.call_soon_threadsafe(bot.loop.stop)  # Stop the bot's event loop
    thread_bot.join()
    print("msg sent, thread joined")


def run_bot_send_msg(msg, channel_id=channel_id_general):
    # print("start")
    command_prefix = "!"
    intents = discord.Intents.default()
    bot = MyBot(
        command_prefix=command_prefix,
        intents=intents,
        message=msg,
        channel_id=channel_id,
    )

    bot.run(discord_notify_Token)
    bot.close_bot()
    print("done")


if __name__ == "__main__":
    # if called by python in cmd
    import sys

    try:
        arg1 = sys.argv[1]
        run_bot_send_msg(arg1)
    except IndexError:
        arg1 = None
        print("no argument, please provide a message in cmd")
