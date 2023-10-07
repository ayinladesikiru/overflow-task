import requests


def print_transfers(transaction_hash: str):
    # transaction_hash
    apikey = "DEVJFIPZ8DXPYW365WM8WS2FNKC67DE3X8"
    # Define the url
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash={transaction_hash}&apikey={apikey}"

    # Send a GET request to the URL and get the response
    response = requests.get(url)
    result = response.json()['result']
    return [{'from': result['from'], 'to': result['to'], 'logs': result['logs']}]


txhash = "0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263"
print(print_transfers(txhash))
