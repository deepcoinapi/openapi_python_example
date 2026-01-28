from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instType': 'SWAP',
    'ccy': 'USDT'
}

res = account_test.get_account_balance(params)