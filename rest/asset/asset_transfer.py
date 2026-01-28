from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'currency_id': 'USDT',
    'amount': '100',
    'from_id': '7',
    'to_id': '1',
    'uid': 'xxx'
}

res = asset_test.asset_transfer(params)