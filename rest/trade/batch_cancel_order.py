from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'OrderSysIDs': ['xxx','xxx']
}

res = trade_test.batch_cancel_order(params)