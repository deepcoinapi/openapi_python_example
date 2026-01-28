from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'account': 'xxx',
    'coin': 'USDT',
    'status': ''
}

res = asset_test.internal_transfer_history(params)