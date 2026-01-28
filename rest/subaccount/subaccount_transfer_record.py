from rest.rest_api import deepcoin_api

subaccount_test = deepcoin_api.SubAccountTest()

params = {
    'coin': 'USDT',
    'fromId': '7',
    'toId': '7',
    'relationType': '1',
    'page': '1',
    'size': '1'
}

res = subaccount_test.sub_account_transfer_record(params)