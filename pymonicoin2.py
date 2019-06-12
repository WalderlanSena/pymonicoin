#   Monitore o valor do Bitcoin nas Exchanges
#   developer: Walderlan Sena
#   code: https://github.com/WalderlanSena/pymonicoin

# Importando modulos
import urllib.request
import json
import time
from datetime import datetime

# Setando a Exchange - FOX - ARN - B2U - BTD - FLW - LOC - MBT -NEG
EXCHANGE  = "FOX"
BTC_PRICE = "last"

def search():
    with urllib.request.urlopen("https://api.bitvalor.com/v1/ticker.json") as url:
        data = json.loads(url.read().decode())
        bitcoinCurrent = data["ticker_24h"]["exchanges"][EXCHANGE][BTC_PRICE]
        print("\033[7;42mVALOR DO BITCOIN >>>\033[0m \033[1;42m ฿: ", bitcoinCurrent,"\033[0m")

print('''
        \033[0;0;33m                                  (_)         (_)
         _ __  _   _ _ __ ___   ___  _ __  _  ___ ___  _ _ __
        | '_ \| | | | '_ ` _ \ / _ \| '_ \| |/ __/ _ \| | '_ \
        | |_) | |_| | | | | | | (_) | | | | | (_| (_) | | | | |
        | .__/ \__, |_| |_| |_|\___/|_| |_|_|\___\___/|_|_| |_|
        | |     __/ |                                    v1.0.0
        |_|    |___/
        \033[0m
                >>> Monitor the value of Bitcoin <<<
                    Developer: Walderlan Sena
            https://github.com/WalderlanSena/pymonicoin
    ''')
search()
while True:
    time.sleep(200)
    search()
