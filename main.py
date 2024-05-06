import requests
from bs4 import BeautifulSoup

url_crypto = 'https://api.coinlore.net/api/ticker/?id=90,80'
url_currency_usd = 'https://www.finmarket.ru/currency/USD/'
url_currency_eur = 'https://www.finmarket.ru/currency/EUR/'


def get_price_btc():
    response = requests.get(url_crypto)
    btc_price = response.json()[0]['price_usd']
    return btc_price


def get_price_eth():
    response = requests.get(url_crypto)
    eth_price = response.json()[1]['price_usd']
    return eth_price


def get_price_usd():
    response = requests.get(url_currency_usd)
    soup = BeautifulSoup(response.text, 'lxml')
    usd_rub = soup.find('div', class_='valvalue').text
    return usd_rub


def get_price_eur():
    response = requests.get(url_currency_eur)
    soup = BeautifulSoup(response.text, 'lxml')
    eur_rub = soup.find('div', class_='valvalue').text
    return eur_rub


def print_price_currency():
    print(
        f'Курс BTC: {get_price_btc()}\nКурс ETH: {get_price_eth()}\nКурс USD: {get_price_usd()}\nКурс EUR: {get_price_eur()}')


if __name__ == '__main__':
    print_price_currency()
