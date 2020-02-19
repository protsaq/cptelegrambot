#!/usr/bin/env python3
from bot import TelegramChatbot
from carol_viaja import train_table_dict
update_id = None

bot = TelegramChatbot("config.cfg")


def make_reply(msg):
    test = ""
    file = train_table_dict()
    if msg is not None:
        with open(file) as f:
            for i in f:
                test += i
    return test


while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
