from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instType': 'SWAP',
    'instId': 'BTC-USDT-SWAP',
    'ordId': '1001119776162185'
}

res = trade_test.cancel_position_sltp(params)