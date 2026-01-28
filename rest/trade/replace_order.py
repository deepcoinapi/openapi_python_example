from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'OrderSysID': 'xxx',
    'price': '83000',
    'volume': '10'
}

res = trade_test.replace_order(params)