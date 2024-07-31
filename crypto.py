import requests
import plotly.graph_objects as go
import matplotlib.pyplot as plt


crypto_symbols = ["BTC", "ETH", "LTC", "DOGE", "XRP"]
dol = 1
my_wallet = {"BTC" : 1,
             "ETH": 1,
             "LTC": 1}

verde = ('\033[1;32m')
amarelob=('\033[1;33m')
azulclaro=('\033[1;34m')
branco=('\033[1;30m')
verdeagua=('\033[1;36m')

def get_price(crypto_symbol):
    
   
    ticker_url = f"https://api.pro.coinbase.com/products/{crypto_symbol}-USD/ticker"
    response = requests.get(ticker_url)
    data = response.json()
    price = float(data['price'])
    return price

def money(n):
    dol = n
    return dol

def check_all():
    btc = int(get_price("BTC"))
    eth = int(get_price("ETH"))
    ltc = int(get_price("LTC"))
    
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nO preço de {amarelob} BITCOIN {azulclaro} atualmente é:  {amarelob}{btc} ${azulclaro}")
    print(f"O preço de  {amarelob}ETH{azulclaro}  atualmente é:  {amarelob}{eth} ${azulclaro}")
    print(f"O preço de  {amarelob}LTC {azulclaro} atualmente é:  {amarelob}{ltc} ${azulclaro}")
    
    a = input(f"\n\npara voltar ao menu digite qualquer coisa\n                     ")
    menu()

def buy():
    print("compra aqui")

    
def sell():
    global dol
    btc = int(get_price("BTC"))
    eth = int(get_price("ETH"))
    ltc = float(get_price("LTC"))
    
    
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nO preço de  {amarelob}BITCOIN{azulclaro}  atualmente é:  {amarelob}{btc} ${azulclaro}")
    print(f"O preço de  {amarelob}ETHEREUM{azulclaro}  atualmente é:  {amarelob}{eth} ${azulclaro}")
    print(f"O preço de  {amarelob}LITECOIN{azulclaro}  atualmente é:  {amarelob}{ltc} ${azulclaro}")
    print(f"\n\n\n\nvocê tem atualmente: {amarelob}{my_wallet['BTC']} Bitcoin{azulclaro} em sua conta")
    print(f"você tem atualmente: {amarelob}{my_wallet['ETH']} Ether{azulclaro} em sua conta")
    print(f"você tem atualmente: {amarelob}{my_wallet['LTC']} LiteCoin{azulclaro} em sua conta\n")
    print(f"\n\ncaso queira voltar ao menu: digite 1\n\n\n\n\n")
    decision = input(f"você quer vender qual crypto? ")
    
    if decision == "1":
        menu()
        
    while True:
        
        if decision.lower() == "btc" or decision.lower() == "bitcoin":
            
            
            if my_wallet["BTC"] == 0:
                print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nnão tem {amarelob}{decision}{azulclaro} pra vender")
                a = input(f"\n\npara voltar ao menu digite qualquer coisa\n                     ")
                menu()
                    
                    
            
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n   O preço de  {amarelob}BITCOIN{azulclaro}  atualmente é:  {amarelob}{btc} ${azulclaro}")
            print(f"   você tem {amarelob}{my_wallet['BTC']} bitcoins{azulclaro} para vender\n\n\n")
            
            venda = int(input("quanto queres vender?  "))
            
            if venda > 0 and venda <= my_wallet["BTC"]:
                my_wallet["BTC"] -= venda
                dol += btc
                print("\n" * 30)
                print(f"você vendeu {amarelob}{venda} BITCOIN{azulclaro} a um preço de {amarelob}{btc}{azulclaro} e agora tem {verde}{dol} dólares.{azulclaro}")
                a = input(f"\n\npara voltar ao menu digite qualquer coisa\n                     ")
                
                menu()
                
        elif decision.lower() == "eth" or decision.lower() == "ethereum" or decision.lower() == "ether":
            
            if my_wallet["ETH"] == 0:
                print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nnão tem {amarelob}{decision}{azulclaro} pra vender")
                a = input(f"\n\npara voltar ao menu digite qualquer coisa\n                     ")
                menu()
                    
                    
            
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n   O preço de  {amarelob}ETHEREUM{azulclaro}  atualmente é:  {amarelob}{eth} ${azulclaro}")
            print(f"\n   você tem {amarelob}{my_wallet['ETH']} ETHEREUM{azulclaro} para vender\n\n\n")
            
            venda = int(input("\nquanto queres vender?"))
            
            if venda > 0 and venda <= my_wallet["ETH"]:
                my_wallet["ETH"] -= venda
                dol += eth
                print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nvocê vendeu {amarelob}{venda} ETHEREUM{azulclaro} a um preço de {amarelob}{eth}{azulclaro} e agora tem {verde}{dol} dólares.{azulclaro}")
                a = input(f"\n\npara voltar ao menu digite qualquer coisa\n                     ")
                
                menu()
                
        elif decision.lower() == "ltc" or decision.lower() == "litecoin":
            if my_wallet["LTC"] >= 0:
                venda = input("quanto queres vender?")
            else:
                print("\n\nNão tens essa moeda, para vender")
        else:
            input("\n\n\n\nessa criptomoeda nao existe, digite qualquer coisa para voltar à vender\n")
            sell()

    

def wallet():
   
    
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    

    
    
    
    print(f"{azulclaro}você tem {verde} {dol} {azulclaro} dólares em sua conta\n")
    print(f"você tem atualmente: {amarelob}{my_wallet['BTC']} Bitcoins {azulclaro} em sua conta")
    print(f"você tem atualmente: {amarelob}{my_wallet['ETH']} Ether {azulclaro} em sua conta")
    print(f"você tem atualmente: {amarelob}{my_wallet['LTC']} LiteCoin {azulclaro} em sua conta")
    
    
    tamanhos = [my_wallet['ETH'], my_wallet['BTC'], my_wallet['LTC']]
    labels = ['ETH', 'BTC', 'LTC']

    plt.pie(tamanhos, labels=labels, autopct='%1.1f%%')
    plt.title('My Crypto Wallet')
    plt.axis('equal')
    plt.show()
    
    input(f"\n\npara voltar ao menu digite qualquer coisa\n                     ")
    menu()
    
    
def menu():
        
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"{verdeagua}    VOCÊ TEM {verde}{dol} DÓLARES{azulclaro} ")
    print(f"  {verdeagua} QUAL {amarelob}AÇÃO{verdeagua} QUER TOMAR?{azulclaro} \n")
    print(f"{amarelob}1){azulclaro} {verdeagua}CHECKAR OS PREÇOS DAS CRYPTOS{azulclaro}\n")
    print(f"{amarelob}2){azulclaro} {verdeagua}COMPRAR ALGUM ATIVO CRYPTO{azulclaro}\n")
    print(f"{amarelob}3){azulclaro} {verdeagua}VENDER ALGUM ATIVO CRYPTO{azulclaro}\n")
    print(f"{amarelob}4){azulclaro} {verdeagua}ANALISAR A MINHA CARTEIRA CRYPTO{azulclaro}\n")
    decision = input(f"")
    if decision == "1":
        check_all()
    if decision == "2":
        buy()
        
    if decision == "3":
        sell()
        
    if decision == "4":
        wallet()
        
if __name__ == "__main__":
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n     BEM VINDO AO SIMULADOR DE CARTEIRA CRYPTO 1.0 BETA  \n")
        print("     VOCÊ QUER COMEÇAR SUA CARTEIRA COM QUANTOS DÓLARES?  \n\n\n")
        try:
            dol = int(input("                       "))
            break
        except:
            pass
    menu()