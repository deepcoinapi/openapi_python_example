from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'bar': '4H',
    # 'after': 'xxx',
    'limit': '1'
}

res = market_test.get_index_kline(params)