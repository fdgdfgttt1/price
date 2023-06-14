import requests

# Cryptocurrency symbols to track
cryptos = ['BTC', 'ETH', 'LTC']

# Price thresholds for each cryptocurrency
price_thresholds = {
    'BTC': {
        'upper': 50000,
        'lower': 40000
    },
    'ETH': {
        'upper': 3000,
        'lower': 2000
    },
    'LTC': {
        'upper': 200,
        'lower': 150
    }
}

# Function to fetch the latest prices of cryptocurrencies from the API
def fetch_crypto_prices():
    try:
        url = 'https://api.coincap.io/v2/assets'
        params = {'ids': ','.join(cryptos)}
        response = requests.get(url, params=params)
        data = response.json()
        prices = {crypto['symbol']: float(crypto['priceUsd']) for crypto in data['data']}
        return prices
    except Exception as e:
        print('Error fetching cryptocurrency prices:', str(e))

# Function to compare the current prices with the previous prices and determine if there's a significant change
def track_crypto_prices():
    previous_prices = {}

    while True:
        current_prices = fetch_crypto_prices()

        if current_prices:
            for crypto in cryptos:
                if crypto in previous_prices:
                    current_price = current_prices[crypto]
                    previous_price = previous_prices[crypto]
                    change_percentage = (current_price - previous_price) / previous_price * 100

                    if change_percentage >= price_thresholds[crypto]['upper']:
                        print(f'{crypto} price has crossed the upper threshold: {current_price}')
                        # Send notification via email or Telegram

                    if change_percentage <= price_thresholds[crypto]['lower']:
                        print(f'{crypto} price has crossed the lower threshold: {current_price}')
                        # Send notification via email or Telegram

                previous_prices[crypto] = current_prices[crypto]

# Start tracking cryptocurrency prices
track_crypto_prices()
