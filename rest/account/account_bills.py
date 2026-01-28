from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instType': 'SWAP',
    'ccy': 'USDT',
    # 'type': 3,
    # 'after': 'xxx',
    # 'before': 'xxx',
    'limit': '10'
}

res = account_test.get_account_bills(params)