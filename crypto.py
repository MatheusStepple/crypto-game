import requests
import matplotlib.pyplot as plt
import pyfiglet
import os

crypto_symbols = ["BTC", "ETH", "LTC", "DOGE", "XRP"]
dol = 0
my_wallet = {"BTC": 1, "ETH": 0, "LTC": 0}

verde = '\033[1;32m'
amarelob = '\033[1;33m'
azulclaro = '\033[1;34m'
branco = '\033[1;30m'
verdeagua = '\033[1;36m'

transaction_history = []

def record_transaction(transaction_type, crypto, amount, price, total_dol):
    global transaction_history
    total_dol = -total_dol if transaction_type == "Compra" else total_dol
    transaction_history.append({
        "type": transaction_type,
        "crypto": crypto,
        "amount": amount,
        "price": price,
        "total_dol": total_dol,
        "balance_after": dol
    })

def history():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not transaction_history:
        print(f"{amarelob}Nenhuma transação registrada.{azulclaro}")
    else:
        print(f"{azulclaro}Histórico de Transações:{azulclaro}")
        recent_transactions = transaction_history[-5:]
        for transaction in recent_transactions:
            transaction_type = transaction['type']
            crypto = transaction['crypto']
            amount = transaction['amount']
            price = transaction['price']
            total_dol = transaction['total_dol']
            balance_after = transaction['balance_after']
            
            if transaction_type == "Compra":
                print(f"{amarelob}Compra{azulclaro} | {crypto} | Quantidade: {amount} | Preço: {price} | Total gasto: {amarelob}{-total_dol:.2f} dólares{azulclaro}")
            elif transaction_type == "Venda":
                print(f"{amarelob}Venda{azulclaro} | {crypto} | Quantidade: {amount} | Preço: {price} | Total ganho: {verde}{total_dol:.2f} dólares{azulclaro}")
            
            print(f"Saldo após a transação: {verde}{balance_after:.2f} dólares{azulclaro}")

    input(f"\n\nPara voltar ao menu digite qualquer coisa\n")
    menu()

def get_price(crypto_symbol):
    ticker_url = f"https://api.pro.coinbase.com/products/{crypto_symbol}-USD/ticker"
    try:
        response = requests.get(ticker_url)
        response.raise_for_status()
        data = response.json()
        return float(data['price'])
    except (requests.RequestException, KeyError, ValueError):
        print(f"{amarelob}Erro ao obter o preço de {crypto_symbol}.{azulclaro}")
        return None

def update_wallet(crypto, amount):
    global dol
    price = get_price(crypto)
    if price is None:
        return
    if amount > 0 and amount <= my_wallet[crypto]:
        my_wallet[crypto] -= amount
        dol += price * amount
        print(f"\nVocê vendeu {amarelob}{amount} {crypto}{azulclaro} a um preço de {amarelob}{price}{azulclaro} e agora tem {verde}{dol:.2f} dólares.{azulclaro}")
    else:
        print(f"\n{amarelob}Quantidade inválida ou insuficiente para vender {crypto}.{azulclaro}")

def buy():
    global dol
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{verdeagua}Você tem {verde}{dol:.2f} dólares{azulclaro}\n")
        
        for symbol in crypto_symbols:
            price = get_price(symbol)
            if price is not None:
                print(f"O preço de {amarelob}{symbol}{azulclaro} atualmente é: {amarelob}${price}{azulclaro}")
        
        decision = input("\nQual criptomoeda você deseja comprar? (BTC/ETH/LTC/DOGE/XRP) ").strip().upper()
        if decision in crypto_symbols:
            try:
                amount_to_buy = float(input(f"Quantos {decision} você deseja comprar? (Ex.: 0.1, 1, 2) "))
                if amount_to_buy <= 0:
                    print(f"\n{amarelob}A quantidade deve ser maior que zero.{azulclaro}")
                    continue
                price = get_price(decision)
                if price is None:
                    continue
                cost = amount_to_buy * price
                if cost > dol:
                    print(f"\n{amarelob}Você não tem dólares suficientes para comprar {amount_to_buy} {decision}.{azulclaro}")
                else:
                    my_wallet[decision] = my_wallet.get(decision, 0) + amount_to_buy
                    dol -= cost
                    record_transaction("Compra", decision, amount_to_buy, price, cost)
                    print(f"\nVocê comprou {amarelob}{amount_to_buy} {decision}{azulclaro} a um preço de {amarelob}${price}{azulclaro} e agora tem {verde}{dol:.2f} dólares.{azulclaro}")
            except ValueError:
                print(f"\n{amarelob}Entrada inválida. Tente novamente.{azulclaro}")
        else:
            print(f"\n{amarelob}Essa criptomoeda não existe.{azulclaro}")
        
        option = input(f"\nDeseja continuar comprando? (Digite 1 para voltar ao menu ou qualquer outra tecla para continuar comprando) ").strip()
        if option == "1":
            menu()
            break

def check_prices():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    prices = {symbol: get_price(symbol) for symbol in crypto_symbols}
    
    print(f"{verdeagua}Preços Atuais das Criptomoedas:{azulclaro}\n")

    max_name_length = max(len(symbol) for symbol in prices.keys())
    
    for symbol, price in prices.items():
        print(f"{symbol.ljust(max_name_length)} : {amarelob}${price:.2f}{azulclaro}" if price is not None else f"{symbol.ljust(max_name_length)} : {amarelob}Erro ao obter o preço{azulclaro}")
    
    print("\n" + "-" * (max_name_length + 20))
    
    input(f"\n{amarelob}Pressione Enter para voltar ao menu...{azulclaro}")
    menu()

def sell():
    global dol
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{verdeagua}Você tem {verde}{dol:.2f} dólares{azulclaro}\n")
        
        for symbol in crypto_symbols:
            price = get_price(symbol)
            if price is not None:
                print(f"O preço de {amarelob}{symbol}{azulclaro} atualmente é: {amarelob}${price}{azulclaro}")

        for symbol, amount in my_wallet.items():
            print(f"Você tem atualmente: {amarelob}{amount} {symbol}{azulclaro} em sua conta")
        
        decision = input("\nQual criptomoeda você deseja vender? (BTC/ETH/LTC/DOGE/XRP) ").strip().upper()
        if decision in my_wallet:
            if my_wallet[decision] == 0:
                print(f"\nVocê não tem {amarelob}{decision}{azulclaro} para vender.")
            else:
                try:
                    amount = float(input(f"Quanto {decision} você quer vender? "))
                    price = get_price(decision)
                    if price is None:
                        continue
                    total_dol = amount * price
                    update_wallet(decision, amount)
                    record_transaction("Venda", decision, amount, price, total_dol)
                except ValueError:
                    print(f"\n{amarelob}Entrada inválida. Tente novamente.{azulclaro}")
        else:
            print(f"\n{amarelob}Essa criptomoeda não existe.{azulclaro}")

        option = input(f"\nDeseja continuar vendendo? (Digite 1 para voltar ao menu ou qualquer outra tecla para continuar vendendo) ").strip()
        if option == "1":
            menu()
            break

def wallet():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{azulclaro}Você tem {verde}{dol:.2f} dólares{azulclaro} em sua conta\n")
    
    total_value = 0
    wallet_details = []
    
    for symbol in crypto_symbols:
        amount = my_wallet.get(symbol, 0)
        price = get_price(symbol)
        if price is not None and amount > 0:
            value = amount * price
            total_value += value
            wallet_details.append((symbol, amount, price, value))
    
    print(f"{azulclaro}Detalhes da sua carteira:{azulclaro}")
    if not wallet_details:
        print(f"\n{amarelob}Nenhuma criptomoeda com valor positivo em sua carteira.{azulclaro}")
    else:
        for symbol, amount, price, value in wallet_details:
            print(f"Você tem atualmente: {amarelob}{amount:.2f} {symbol}{azulclaro} | Preço atual: {amarelob}${price:.2f}{azulclaro} | Valor total: {verde}${value:.2f}{azulclaro}")
        
        print(f"\n{verdeagua}Valor total da sua carteira: {verde}${total_value:.2f}{azulclaro}")

        sizes = [value for _, _, _, value in wallet_details if value > 0]
        labels = [f"{symbol} ({amount:.2f})" for symbol, amount, _, value in wallet_details if value > 0]
        
        if sizes:
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title('Distribuição da Carteira Crypto')
            plt.axis('equal')
            plt.show()
        else:
            print(f"\n{amarelob}Nenhuma criptomoeda com valor positivo para exibir no gráfico.{azulclaro}")
    
    input("Pressione Enter para continuar...")
    menu()

def reset_game():
    global dol, my_wallet, transaction_history
    dol = 0
    my_wallet = {"BTC": 1, "ETH": 0, "LTC": 0, "DOGE": 0, "XRP": 0}
    transaction_history = []
    menu()

def retire():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    initial_value = get_price("BTC")
    if initial_value is None:
        print(f"{amarelob}Erro ao obter o preço do Bitcoin inicial.{azulclaro}")
        return
    
    current_value = dol
    for symbol in crypto_symbols:
        price = get_price(symbol)
        if price is not None:
            current_value += my_wallet.get(symbol, 0) * price
    
    profit_or_loss = current_value - initial_value
    porcentagem = (current_value / initial_value) - 1 
    
    print(f"{verdeagua}Você decidiu se aposentar!{azulclaro}")
    print(f"\n{verde}Saldo Inicial (1 BTC): {amarelob}${initial_value:.2f}{azulclaro}")
    print(f"{verde}Saldo Atual (em dólares e cripto): {amarelob}${current_value:.2f}{azulclaro}")
    
    if profit_or_loss > 0:
        
        print(f"{verde}Lucro: {amarelob}{porcentagem:.4f}%{azulclaro}")
    else:
        print(f"{verde}Prejuízo: {amarelob}${-profit_or_loss:.2f}{azulclaro}")
    
    option = input(f"\n{amarelob}Deseja jogar novamente? (Digite 'sim' para reiniciar ou qualquer outra tecla para sair){azulclaro} ").strip().lower()
    if option == 'sim':
        reset_game()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        # print(f"\n{amarelob}Obrigado por jogar!\n\n")
        print(f"{amarelob}")
        print("""\

      _.-^^---....,,--       
 _--                  --_  
<                        >)
|   Thanks For Playing!   | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____


                    """)
        print(f"\n  CREDITS\n\n")
        print(f'BETA TESTERS:\n\nMATHEUS "{verde}poohzao{amarelob}" HENRIQUE\n\nPAULO "{verde}caradasluzes{amarelob}" HENRIQUE\n\n\n\n\n\n\n\n\n\n\n')


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{verdeagua}Você tem {verde}{dol:.2f} dólares{azulclaro}")
    print(f"{verdeagua}Qual {amarelob}ação{verdeagua} quer tomar?{azulclaro}\n")
    print(f"{amarelob}1){azulclaro} {verdeagua}Verificar os preços das criptos{azulclaro}\n")
    print(f"{amarelob}2){azulclaro} {verdeagua}Comprar algum ativo crypto{azulclaro}\n")
    print(f"{amarelob}3){azulclaro} {verdeagua}Vender algum ativo crypto{azulclaro}\n")
    print(f"{amarelob}4){azulclaro} {verdeagua}Analisar a minha carteira crypto{azulclaro}\n")
    print(f"{amarelob}5){azulclaro} {verdeagua}Ver meu histórico de transações{azulclaro}\n")
    print(f"{amarelob}6){azulclaro} {verdeagua}se aposentar{azulclaro}\n")
    

    
    decision = input("Escolha uma opção: ").strip()
    if decision == "1":
        check_prices()
    elif decision == "2":
        buy()
    elif decision == "3":
        sell()
    elif decision == "4":
        wallet()
    elif decision == "5":
        history()
    elif decision == "6":
        retire()
        
    else:
        print(f"\n{amarelob}Opção inválida.{azulclaro}")
        input("Pressione Enter para tentar novamente...")
        menu()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{amarelob}")
    result = pyfiglet.figlet_format("CRYPTO GAME", font="univers")
    arroz = pyfiglet.figlet_format("A crypto wallet simulator", font="straight")
    
    print(result)
    print(arroz)
    
    input(f"{azulclaro}Pressione Enter para continuar...")
    menu()
