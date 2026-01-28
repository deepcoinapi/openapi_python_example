from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instType': 'SwapU',
    'instId': 'BTCUSDT'
}

res = trade_test.get_history_funding_rate(params)