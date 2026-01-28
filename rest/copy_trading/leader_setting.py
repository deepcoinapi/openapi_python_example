from rest.rest_api import deepcoin_api

copy_trading_test = deepcoin_api.CopyTradingTest()

params = {
    'status': 1,
    'homeMode': 3,
    # 'isClosedCopyCode': True,
    # 'copyCode': 'xxx'
}

res = copy_trading_test.leader_settings(params)