from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'symbol': 'BTC-USDT-SWAP',
    'stime': '1700000000',
    # 'etime': '',
    'limit': '5'
}

res = market_test.get_handicap_trade(params)