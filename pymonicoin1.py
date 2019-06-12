#   Monitore o valor do Bitcoin nas Exchanges/ Monitor the value of Bitcoin
#   developer: Walderlan Sena
#   code: https://github.com/WalderlanSena/pymonicoin
#   version: v1.2.0
#   license: MIT license

import urllib.request
import json
import time
from datetime import datetime

# Setando a Exchange - FOX - ARN - B2U - BTD - FLW - LOC - MBT -NEG
EXCHANGE  = "FOX"
BTC_PRICE = "last"

def returnDate():
    hj = datetime.today()
    data = str("[ ") + str(hj.day) + str("/") + str(hj.month) + str("/") + str(hj.year) + str(" ]")
    return data

def returnHour():
    horaAtual = datetime.now()
    hora      = horaAtual.hour
    minuto    = horaAtual.minute
    segundos  = horaAtual.second

    horaPrint = "[ " + str(hora) + ":" + str(minuto) + ":" + str(segundos) + " ]"
    return horaPrint

bitcoinDepositado = float('254.0')
bitcoinInit       = float('68.998')

def request():
    with urllib.request.urlopen("https://api.bitvalor.com/v1/ticker.json") as url:
        data = json.loads(url.read().decode())
        bitcoinCurrent = data["ticker_24h"]["exchanges"][EXCHANGE][BTC_PRICE]
        bitCalcTemp    = float(bitcoinCurrent*bitcoinDepositado)
        bitcoinFinal   = str(float(bitCalcTemp/bitcoinInit))

        with open('bit.log', 'a') as arq:
            arq.write("VALOR DO BITCOIN >>> " + str(bitcoinCurrent)  + "\tGANHO EM REAL >>> " + bitcoinFinal[0:6] + " " + returnDate() + " " + returnHour() + "\n")
            arq.close()

        print("\033[7;42mVALOR DO BITCOIN >>>\033[0m \033[1;42m ฿: ", bitcoinCurrent,"\033[0m\t", "\033[7;42mGANHO EM REAL >>>\033[0m \033[1;42m R$: ", bitcoinFinal[0:6],"\033[0m", returnHour())

def splash():
    print('''
            \033[0;0;33m                                  (_)         (_)
             _ __  _   _ _ __ ___   ___  _ __  _  ___ ___  _ _ __
            | '_ \| | | | '_ ` _ \ / _ \| '_ \| |/ __/ _ \| | '_ \
            | |_) | |_| | | | | | | (_) | | | | | (_| (_) | | | | |
            | .__/ \__, |_| |_| |_|\___/|_| |_|_|\___\___/|_|_| |_|
            | |     __/ |                                    v1.2.0
            |_|    |___/
            \033[0m
                    >>> Monitor the value of Bitcoin <<<
                        Developer: Walderlan Sena
                https://github.com/WalderlanSena/pymonicoin
        ''')

def main():
    splash()
    request()
    while True:
        time.sleep(200)
        request()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt):
        print("\n by...")
