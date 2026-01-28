from rest.rest_api import deepcoin_api

copy_trading_test = deepcoin_api.CopyTradingTest()

params = {
    'positionType': '1'
}

res = copy_trading_test.post_position_type(params)