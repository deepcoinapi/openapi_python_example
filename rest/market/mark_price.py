from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'instType': 'SWAP',
    # 'uly': 'BTC-USDT',
    'instId': 'BTC-USDT-SWAP'
}

res = market_test.get_mark_price(params)