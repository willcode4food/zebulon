import os
import csv

from datetime import datetime
from threading import Timer

import time


from CoinbaseProClient import CBPRestClient
from CoinbaseProClient import CBPSocketClient


api_key = os.environ.get('COINBASE_API_KEY')
api_secret = os.environ.get('COINBASE_SECRET')
api_passphrase = os.environ.get('COINBASE_PASSPHRASE')


# Uncomment for REST Client

# fetch = CBPRestClient(api_key, api_secret, api_passphrase)

# response = fetch('GET', 'product_trades_btc', '').json()
# print(response)

socket = CBPSocketClient(api_key, api_secret, api_passphrase)


@socket.subscribe
def on_message(message, message_index):

    if message_index == 2:
        header = message.keys()

        csv_writer.writerow(header)
    values = message.values()
    csv_writer.writerow(message.values())
    print(values)


def exitfunc():
    csv_writer.writerow("Exit Time" + str(datetime.now()))
    trades.close()
    os._exit(0)


# run for 900 seconds (15 minutes)
Timer(900, exitfunc).start()

trades = open('trades.csv', 'w')
csv_writer = csv.writer(trades)
print("Start Time", datetime.now())
socket(["BTC-USD"])
