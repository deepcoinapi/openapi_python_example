from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'coin': 'USDT',
    # 'txHash': 'xxx',
    # 'startTime': 'xxx',
    # 'endTime': 'xxx',
    # 'page': 'xxx',
    # 'size': 'xxx'
}

res = asset_test.deposit_list(params)