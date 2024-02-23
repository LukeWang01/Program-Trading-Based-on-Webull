from discord_notify_bot import run_bot_send_msg, run_bot_send_msg_new_thread

import json
import hashlib
import time

from env._secrete import channel_id_transaction

"""
This script is used to send notification to discord channel when the trading_actions.json file is updated.
Any new placed order will be sent to the discord channel.
"""


def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)  # Read in 64k chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


# JSON file path
json_file_path = "../trader/trading_actions.json"

# Record the initial state
initial_json_state = read_json_file(json_file_path)
print(initial_json_state[-1])
initial_json_hash = calculate_file_hash(json_file_path)
print(initial_json_hash)


while True:
    # Check if the file has changed
    current_json_hash = calculate_file_hash(json_file_path)

    if current_json_hash != initial_json_hash:
        print("JSON file has changed.")
        new_json_state = read_json_file(json_file_path)

        # Process the new JSON data as needed
        print("New JSON Data:", new_json_state[-1])
        msg = f"-------------------------"
        msg += new_json_state[-1]["order_time"] + "\n"
        msg += f"account_id: {new_json_state[-1]['stock']} \n"
        msg += f"{new_json_state[-1]['order_direction']}: {new_json_state[-1]['stock_info']} \n"
        msg += f"Price: {new_json_state[-1]['order_price']} \n"
        msg += f"Qty: {new_json_state[-1]['order_qty']} \n"
        msg += f"Total Cost: {new_json_state[-1]['order_cost']} \n"
        msg += f"-------------------------"

        run_bot_send_msg_new_thread(msg, channel_id=channel_id_transaction)

        # Update the recorded state and hash
        initial_json_state = new_json_state
        initial_json_hash = current_json_hash

    # Sleep for a while (e.g., every 10 seconds)
    time.sleep(10)
