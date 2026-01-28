from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instType': 'SWAP',
    'instId': 'BTC-USDT-SWAP',
    'OrderType': 'limit',
    'limit': 100
}

res = trade_test.trigger_orders_history(params)