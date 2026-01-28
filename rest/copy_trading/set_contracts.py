from rest.rest_api import deepcoin_api

copy_trading_test = deepcoin_api.CopyTradingTest()

params = {
    'contracts': 'BTCUSDT'
}

res = copy_trading_test.set_contracts(params)