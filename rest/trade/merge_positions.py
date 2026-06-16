from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'posIds': '[xxx,xxx]',
}

res = trade_test.merge_positions(params)