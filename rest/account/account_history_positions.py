from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instType': 'SWAP',
    # 'instId': 'BTC-USDT-SWAP',
    # 'mgnMode': 'cross',
    # 'mrgPosition': 'merge',
    # 'posId': '',
    # 'startTime': '',
    # 'endTime': '',
    # 'limit': '100'
}

res = account_test.get_history_positions(params)
print(res)
