# Auto send message to discord channel via web request
import requests

from env._secrete import (
    channel_id_general,
    discord_web_Auth,
    channel_id_strategy,
    channel_id_transaction,
    discord_notify_Token,
)


def send_msg_to_discord_request(msg, channel_id=channel_id_general, auth=discord_web_Auth):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    payload = {
        "content": msg,
    }

    header = {
        'Authorization': auth,
    }

    r = requests.post(url, data=payload, headers=header)

    print(r)


if __name__ == '__main__':
    # channel_id_general
    # channel_id_transaction
    # channel_id_strategy
    send_msg_to_discord_request("test 01", channel_id_general, discord_web_Auth)

