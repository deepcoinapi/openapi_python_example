from rest.rest_api import deepcoin_api

copy_trading_test = deepcoin_api.CopyTradingTest()

params = {
    'status': 1
}

res = copy_trading_test.follower_rank(params)