from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'wdId': '339288',
    'ccy': 'USDT',
    'clientId': 'withdraw_python_example_001',
}

res = asset_test.cancel_withdraw(params)