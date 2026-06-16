from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'bar': '4H',
    # 'startTime': 'xxx',
    # 'endTime': 'xxx',
    'limit': '10'
}

res = market_test.get_long_short_ratio(params)