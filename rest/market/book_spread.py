from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'value': 1,
    'vType': '0'
}

res = market_test.get_book_spread(params)