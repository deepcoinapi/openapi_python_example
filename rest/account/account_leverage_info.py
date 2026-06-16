from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'mgnMode': 'cross',
    'mrgPosition': 'merge'
}

res = account_test.get_leverage_info(params)
print(res)
