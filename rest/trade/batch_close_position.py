from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'productGroup': 'SwapU',
    'instId': 'BTC-USDT-SWAP'
}

res = trade_test.batch_close_position(params)