from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'ordId': 'xxx',
    # 'clOrdId': 'xxx'
}

res = trade_test.cancel_trigger_order(params)