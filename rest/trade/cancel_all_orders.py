from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'InstrumentID': 'BTCUSDT',
    'ProductGroup': 'SwapU',
    'IsCrossMargin': '1',
    'IsMergeMode': '1'
}

res = trade_test.cancel_all_orders(params)