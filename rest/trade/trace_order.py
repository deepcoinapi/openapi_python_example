from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'retracePoint': '1000',
    'triggerPrice': '-1',
    'posSide': 'long'
}

res = trade_test.trace_order(params)