from crypto import get_action_function, check_prices, buy, sell, wallet, history, retire, check_crypto_exists, can_afford, dol

crypto_symbols = ["BTC", "ETH", "LTC", "DOGE", "XRP"]


def test_get_action_function():
   
    assert get_action_function("1") == check_prices
    assert get_action_function("2") == buy
    assert get_action_function("3") == sell
    assert get_action_function("4") == wallet
    assert get_action_function("5") == history
    assert get_action_function("6") == retire
    assert get_action_function("7") is None
    assert get_action_function("") is None
    


def test_check_crypto_exists():
 
    assert check_crypto_exists("BTC") is True
    assert check_crypto_exists("ETH") is True
    assert check_crypto_exists("LTC") is True
    assert check_crypto_exists("DOGE") is True
    assert check_crypto_exists("XRP") is True
    assert check_crypto_exists("DOLAR") is False
    assert check_crypto_exists("EURO") is False
    assert check_crypto_exists("YEN") is False
    
def test_can_afford():
    global dol
    
    dol = 1000
    amount = 2  
    price = 400 
    
    assert can_afford(amount, price) == True
    
    dol = 1000
    amount = 1  
    price = 1000
    
    assert can_afford(amount, price) == True
    
    dol = 1000
    amount = 3  
    price = 300 
    
    assert can_afford(amount, price) == True
    
    dol = 1000
    amount = 4  
    price = 300 
    
    assert can_afford(amount, price) == False
    
    
    
    
    

   
    
    
    
    
