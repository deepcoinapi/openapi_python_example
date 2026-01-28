from rest.rest_api import deepcoin_api

subaccount_test = deepcoin_api.SubAccountTest()

params = {
    'fromUid': 'xxx',
    'toUid': 'xxx',
    'fromId': '7',
    'toId': '7',
    'amount': '100',
    'coin': 'USDT'
}

res = subaccount_test.sub_account_transfer(params)