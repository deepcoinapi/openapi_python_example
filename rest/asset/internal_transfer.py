from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'coin': 'USDT',
    'amount': '100',
    'receiverAccount': 'xxx',
    'accountType': 'xxx',
    'receiverUID': 'xxx'
}

res = asset_test.internal_transfer(params)