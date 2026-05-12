from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'ccy': 'USDT',
    'chain': 'USDT-TRC20',
    'amt': 1,
    'addressId': '574',
    'toAddr': 'TEV1gDkDST3kUtv27SCYfbAoz7ukLMwJdS',
    'memo': 'xxx',
    'accountTypes': ['funding'],
    'clientId': 'withdraw_python_example_001',
    'remark': 'python example withdrawal'
}

res = asset_test.withdraw(params)