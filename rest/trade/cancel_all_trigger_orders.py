from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'ProductGroup': 'SwapU',
    'InstrumentID': 'BTCUSDT',
    'IsCrossMargin': '1',
    'IsMergeMode': '1'
}

res = trade_test.cancel_all_trigger_orders(params)