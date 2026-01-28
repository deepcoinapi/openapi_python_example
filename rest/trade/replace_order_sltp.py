from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'orderSysID': 'xxx',
    'tpTriggerPx': '99000',
    'slTriggerPx': '80000'
}

res = trade_test.replace_order_sltp(params)