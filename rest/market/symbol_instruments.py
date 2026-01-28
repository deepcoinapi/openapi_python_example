from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'instType': 'SWAP',
    'instId': 'BTC-USDT-SWAP',
    'uly': '',
}

res = market_test.get_instruments(params)