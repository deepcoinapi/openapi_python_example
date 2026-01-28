from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'sz': '3'
}

res = market_test.get_orderbook(params)