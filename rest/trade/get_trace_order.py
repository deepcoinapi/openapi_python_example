from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instId': 'BTC-USDT-SWAP'
}

res = trade_test.trace_order_list(params)