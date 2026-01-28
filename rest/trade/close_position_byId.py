from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'productGroup': 'SwapU',
    'instId': 'BTC-USDT-SWAP',
    'positionIds': ['xxx']
}

res = trade_test.close_position_by_ids(params)