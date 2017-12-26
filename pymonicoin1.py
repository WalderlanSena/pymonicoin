#   Monitore o valor do Bitcoin nas Exchanges/ Monitor the value of Bitcoin
#   developer: Walderlan Sena
#   code: https://github.com/WalderlanSena/pymonicoin
#   version: v1.2.0
#   license: MIT license

# Importando modulos 
import urllib.request
import json
import time
from datetime import datetime

# Setando a Exchange - FOX - ARN - B2U - BTD - FLW - LOC - MBT -NEG
EXCHANGE  = "FOX"
BTC_PRICE = "last"

# Funcao que retorna data atual
def returnDate():
    hj = datetime.today()
    data = str("[ ") + str(hj.day) + str("/") + str(hj.month) + str("/") + str(hj.year) + str(" ]")
    return data

# Funcao que retorna a hora atual do sistema
def returnHour():
    horaAtual = datetime.now()

    hora      = horaAtual.hour
    minuto    = horaAtual.minute
    segundos  = horaAtual.second

    # Formatando impressao do hora atual
    horaPrint = "[ " + str(hora) + ":" + str(minuto) + ":" + str(segundos) + " ]"
    return horaPrint

# Valor do bitcoin depositado em real
bitcoinDepositado = float('254.0')
# Valor do bitcoin no momento do deposito anterior
bitcoinInit       = float('68.998')

# Função que realiza a requisição
def request():
    # Realiza a requisicao para a api que retorna o json com o valor do bitcoin atualmente
    with urllib.request.urlopen("https://api.bitvalor.com/v1/ticker.json") as url:
        # Atribuindo a variavel data o decode da requisicao
        data = json.loads(url.read().decode())
        # Recebe o valor do bitcoin atualmente
        bitcoinCurrent = data["ticker_24h"]["exchanges"][EXCHANGE][BTC_PRICE]
        # Recebe a multiplicacao do valor do bitcoin atualmente * o valor do bitcoin depositado
        bitCalcTemp    = float(bitcoinCurrent*bitcoinDepositado)
        # Recebe valor final da divisao do resultado da multiplicacao * o valor do bitcoin na hora do deposito
        bitcoinFinal   = str(float(bitCalcTemp/bitcoinInit))
        
        # Escrevendo no arquivo de log
        with open('bit.log', 'a') as arq:
            # Escrevendo arquivo
            arq.write("VALOR DO BITCOIN >>> " + str(bitcoinCurrent)  + "\tGANHO EM REAL >>> " + bitcoinFinal[0:6] + " " + returnDate() + " " + returnHour() + "\n")
            # Fechando o arquivo cujo contem as informacoes de log
            arq.close()
        
        # Imprimindo na tela os valores obtido
        print("\033[7;42mVALOR DO BITCOIN >>>\033[0m \033[1;42m ฿: ", bitcoinCurrent,"\033[0m\t", "\033[7;42mGANHO EM REAL >>>\033[0m \033[1;42m R$: ", bitcoinFinal[0:6],"\033[0m", returnHour())

def splash():
    # Tela de Splash
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
    # Chamando tela de splash
    splash()
    # Realiza uma requisição incial
    request()
    # Laço infinito
    while True:
        # Esperando 200 segundos para fazer uma requisicao
        time.sleep(200)
        # Chamando a funcao que faz a requisicao
        request()
    # end while

# Init software
if __name__ == "__main__":
    try:
        # Chamando a funcao main
        main()
    except (KeyboardInterrupt):
        # Mostra o texto posterior caso o usuario interrompa o software
        print("\n by...")
