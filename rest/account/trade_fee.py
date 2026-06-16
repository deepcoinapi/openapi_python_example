from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instType': 'SWAP',
    'instId': 'BTC-USDT-SWAP',
    # 'instFamily': 'BTC-USDT',
    # 'groupId': ''
}

res = account_test.get_trade_fee(params)