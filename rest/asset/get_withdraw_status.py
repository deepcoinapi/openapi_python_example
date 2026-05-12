from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'wdId': 'xxx',
    'ccy': 'USDT',
}

res = asset_test.withdraw_status(params)