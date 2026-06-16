from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'accountType': 'funding,spot,swapU',
    'ccy': 'USDT'
}

res = account_test.get_all_balances(params)