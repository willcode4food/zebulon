import os

from CoinbaseProClient import CBPRestClient
from CoinbaseProClient import CBPSocketClient


api_key = os.environ.get('COINBASE_API_KEY')
api_secret = os.environ.get('COINBASE_SECRET')
api_passphrase = os.environ.get('COINBASE_PASSPHRASE')


# fetch = CBPRestClient(api_key, api_secret, api_passphrase)

# response = fetch('GET', 'product_trades_btc', '').json()
# print(response)

socket = CBPSocketClient(api_key, api_secret, api_passphrase)


@socket.subscribe
def on_message(message):
    print(message)


socket(["BTC-USD"])
