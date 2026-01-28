from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'lever': '30',
    'mgnMode': 'cross',
    'mrgPosition': 'merge'
}

res = account_test.post_set_leverage(params)