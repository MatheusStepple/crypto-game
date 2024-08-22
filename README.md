 # YOUR PROJECT TITLE
  #### Video Demo: https://www.youtube.com/watch?v=GG1J5cnt9Eg
  #### Description: Final project for Harvard University's CS50 Introduction to Programming with Python. Through the use of real-time APIs, players experience the thrill of buying and selling virtual cryptocurrencies based on live exchange rates. The game not only provides a hands-on understanding of cryptocurrency trading but also challenges players to make strategic decisions in a fluctuating market environment.API Documentation
Record a Transaction

POST /api/transactions
## API Documentation

#### Record a Transaction

```http
  POST /api/transactions
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `transaction_type` | `string` | Required. The type of transaction, e.g., "Buy" or "Sale". |
| `crypto` | `string` | Required. The cryptocurrency symbol, e.g., "BTC". |
| `amount` | `string` | Required. The amount of cryptocurrency involved in the transaction. |
| `price` | `string` | Required. The price per unit of the cryptocurrency. |
| `total_value` | `string` | Required. The total value of the transaction. |


#### Get Cryptocurrency Price

```http
  GET /api/items/${id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `crypto_symbol`      | `string` | Required. The cryptocurrency symbol, e.g., "BTC". |

#### Buy Cryptocurrency
POST /api/buy
#### Sell Cryptocurrency
POST /api/sell
#### Get Transaction History
POST /api/history
#### Get Wallet
POST /api/wallet


## Running Tests

To run the tests, use the following command:

```bash
  pytest
```


## 🚀 About me
Matheus Stepple is a software developer actively completing Harvard's CS50 Introduction to Programming with Python course. He is working on projects like a cryptocurrency simulation game, demonstrating his skills in backend development and API integration. Matheus is committed to leveraging his growing expertise to create innovative and engaging software solutions.

