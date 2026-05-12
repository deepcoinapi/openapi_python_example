from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'coin': 'USDT',
    # 'ccy': 'USDT',
    'chain': 'USDT-TRC20',
    # 'txHash': 'xxx',
    # 'txId': 'xxx',
    # 'wdId': 'xxx',
    # 'state': 1,
    # 'startTime': 'xxx',
    # 'endTime': 'xxx',
    # 'page': 'xxx',
    # 'size': 'xxx'
}

res = asset_test.withdraw_list(params)