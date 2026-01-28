from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instType': 'SWAP',
    'istId': 'BTC-USDT-SWAP'
}

res = account_test.get_account_positions(params)