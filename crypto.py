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
        print(f"{amarelob}No transactions recorded.{azulclaro}")
    else:
        print(f"{azulclaro}Transaction History:{azulclaro}")
        recent_transactions = transaction_history[-5:]
        for transaction in recent_transactions:
            transaction_type = transaction['type']
            crypto = transaction['crypto']
            amount = transaction['amount']
            price = transaction['price']
            total_dol = transaction['total_dol']
            balance_after = transaction['balance_after']
            
            if transaction_type == "Compra":
                print(f"{amarelob}Buy{azulclaro} | {crypto} | Amount: {amount} | Price: {price} | Total spent: {amarelob}{-total_dol:.2f} dollars{azulclaro}")
            elif transaction_type == "Venda":
                print(f"{amarelob}Sell{azulclaro} | {crypto} | Amount: {amount} | Price: {price} | Total earned: {verde}{total_dol:.2f} dollars{azulclaro}")
            
            print(f"Balance after transaction: {verde}{balance_after:.2f} dollars{azulclaro}")

    input(f"\n\nPress any key to return to the menu\n")
    menu()

def get_price(crypto_symbol):
    ticker_url = f"https://api.pro.coinbase.com/products/{crypto_symbol}-USD/ticker"
    try:
        response = requests.get(ticker_url)
        response.raise_for_status()
        data = response.json()
        return float(data['price'])
    except (requests.RequestException, KeyError, ValueError):
        print(f"{amarelob}Error getting the price of {crypto_symbol}.{azulclaro}")
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
        print(f"{verdeagua}You have {verde}{dol:.2f} dollars{azulclaro}\n")
        
        for symbol in crypto_symbols:
            price = get_price(symbol)
            if price is not None:
                print(f"The price of {amarelob}{symbol}{azulclaro} currently is: {amarelob}${price}{azulclaro}")
        
        decision = input("\nWhich cryptocurrency do you want to buy? (BTC/ETH/LTC/DOGE/XRP) ").strip().upper()
        if decision in crypto_symbols:
            try:
                amount_to_buy = float(input(f"How much {decision} do you want to buy? (e.g., 0.1, 1, 2) "))
                if amount_to_buy <= 0:
                    print(f"\n{amarelob}The amount must be greater than zero.{azulclaro}")
                    continue
                price = get_price(decision)
                if price is None:
                    continue
                cost = amount_to_buy * price
                if cost > dol:
                    print(f"\n{amarelob}You don't have enough dollars to buy {amount_to_buy} {decision}.{azulclaro}")
                else:
                    my_wallet[decision] = my_wallet.get(decision, 0) + amount_to_buy
                    dol -= cost
                    record_transaction("Buy", decision, amount_to_buy, price, cost)
                    print(f"\nYou bought {amarelob}{amount_to_buy} {decision}{azulclaro} at a price of {amarelob}${price}{azulclaro} and now have {verde}{dol:.2f} dollars.{azulclaro}")
            except ValueError:
                print(f"\n{amarelob}Invalid input. Please try again.{azulclaro}")
        else:
            print(f"\n{amarelob}This cryptocurrency does not exist.{azulclaro}")
        
        option = input(f"\nDo you want to continue buying? (Enter 1 to return to the menu or any other key to continue buying) ").strip()
        if option == "1":
            menu()
            break

def check_prices():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    prices = {symbol: get_price(symbol) for symbol in crypto_symbols}
    
    print(f"{verdeagua}Current Cryptocurrency Prices:{azulclaro}\n")

    max_name_length = max(len(symbol) for symbol in prices.keys())
    
    for symbol, price in prices.items():
        print(f"{symbol.ljust(max_name_length)} : {amarelob}${price:.2f}{azulclaro}" if price is not None else f"{symbol.ljust(max_name_length)} : {amarelob}Erro ao obter o preço{azulclaro}")
    
    print("\n" + "-" * (max_name_length + 20))
    
    input(f"{azulclaro}Press Enter to continue...")
    menu()

def sell():
    global dol
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{verdeagua}You have {verde}{dol:.2f} dollars{azulclaro}\n")
        
        for symbol in crypto_symbols:
            price = get_price(symbol)
            if price is not None:
                print(f"The price of {amarelob}{symbol}{azulclaro} is currently: {amarelob}${price}{azulclaro}")

        for symbol, amount in my_wallet.items():
            print(f"You currently have: {amarelob}{amount} {symbol}{azulclaro} in your account")
        
        decision = input("\nWhich cryptocurrency would you like to sell? (BTC/ETH/LTC/DOGE/XRP) ").strip().upper()
        if decision in my_wallet:
            if my_wallet[decision] == 0:
                print(f"\nYou don't have any {amarelob}{decision}{azulclaro} to sell.")
            else:
                try:
                    amount = float(input(f"How much {decision} do you want to sell? "))
                    price = get_price(decision)
                    if price is None:
                        continue
                    total_dol = amount * price
                    update_wallet(decision, amount)
                    record_transaction("Sale", decision, amount, price, total_dol)
                except ValueError:
                    print(f"\n{amarelob}Invalid input. Please try again.{azulclaro}")
        else:
            print(f"\n{amarelob}This cryptocurrency does not exist.{azulclaro}")

        option = input(f"\nDo you want to continue selling? (Type 1 to go back to the menu or any other key to continue selling) ").strip()
        if option == "1":
            menu()
            break

def wallet():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{azulclaro}You have {verde}{dol:.2f} dollars{azulclaro} in your account\n")
    
    total_value = 0
    wallet_details = []
    
    for symbol in crypto_symbols:
        amount = my_wallet.get(symbol, 0)
        price = get_price(symbol)
        if price is not None and amount > 0:
            value = amount * price
            total_value += value
            wallet_details.append((symbol, amount, price, value))
    
    print(f"{azulclaro}Details of your wallet:{azulclaro}")
    if not wallet_details:
        print(f"\n{amarelob}No cryptocurrency with positive value in your wallet.{azulclaro}")
    else:
        for symbol, amount, price, value in wallet_details:
            print(f"You currently have: {amarelob}{amount:.2f} {symbol}{azulclaro} | Current price: {amarelob}${price:.2f}{azulclaro} | Total value: {verde}${value:.2f}{azulclaro}")
        
        print(f"\n{verdeagua}Total value of your wallet: {verde}${total_value:.2f}{azulclaro}")

        sizes = [value for _, _, _, value in wallet_details if value > 0]
        labels = [f"{symbol} ({amount:.2f})" for symbol, amount, _, value in wallet_details if value > 0]
        
        if sizes:
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title('Crypto Wallet Distribution')
            plt.axis('equal')
            plt.show()
        else:
            print(f"\n{amarelob}No cryptocurrency with positive value to display on the chart.{azulclaro}")
    
    input(f"{azulclaro}Press Enter to continue...")
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
        print(f"{amarelob}Error getting initial Bitcoin price.{azulclaro}")
        return
    
    current_value = dol
    for symbol in crypto_symbols:
        price = get_price(symbol)
        if price is not None:
            current_value += my_wallet.get(symbol, 0) * price
    
    profit_or_loss = current_value - initial_value
    percentage = (current_value / initial_value) - 1 
    
    print(f"{verdeagua}You decided to retire!{azulclaro}")
    print(f"\n{verde}Initial Balance (1 BTC): {amarelob}${initial_value:.2f}{azulclaro}")
    print(f"{verde}Current Balance (in dollars and crypto): {amarelob}${current_value:.2f}{azulclaro}")
    
    if profit_or_loss > 0:
        print(f"{verde}Profit: {amarelob}{percentage:.4f}%{azulclaro}")
    else:
        print(f"{verde}Loss: {amarelob}${-profit_or_loss:.2f}{azulclaro}")
    
    option = input(f"\n{amarelob}Do you want to play again? (Type 'yes' to restart or any other key to exit){azulclaro} ").strip().lower()
    if option == 'yes':
        reset_game()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
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
    print(f"{verdeagua}You have {verde}{dol:.2f} dollars{azulclaro}")
    print(f"{verdeagua}What {amarelob}action{verdeagua} would you like to take?{azulclaro}\n")
    print(f"{amarelob}1){azulclaro} {verdeagua}Check crypto prices{azulclaro}\n")
    print(f"{amarelob}2){azulclaro} {verdeagua}Buy a crypto asset{azulclaro}\n")
    print(f"{amarelob}3){azulclaro} {verdeagua}Sell a crypto asset{azulclaro}\n")
    print(f"{amarelob}4){azulclaro} {verdeagua}Analyze my crypto wallet{azulclaro}\n")
    print(f"{amarelob}5){azulclaro} {verdeagua}View my transaction history{azulclaro}\n")
    print(f"{amarelob}6){azulclaro} {verdeagua}Retire{azulclaro}\n")
    
    decision = input("Choose an option: ").strip()
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
        print(f"\n{amarelob}Invalid option.{azulclaro}")
        input(f"{azulclaro}Press Enter to continue...")
        menu()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{amarelob}")
    result = pyfiglet.figlet_format("CRYPTO GAME", font="univers")
    arroz = pyfiglet.figlet_format("A crypto wallet simulator", font="straight")
    
    print(result)
    print(arroz)
    
    input(f"{azulclaro}Press Enter to continue...")
    menu()
