from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'posId': 'xxx',
    'ordType': 'market',
    'sz': 1,
    'px': '50000'
}

res = trade_test.merge_positions(params)