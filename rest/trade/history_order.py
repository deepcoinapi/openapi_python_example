from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instType': 'SWAP',
    # 'instId': 'BTC-USDT-SWAP',
    # 'ordType': 'market',
    # 'state': 'filled',
    # 'after': 'xxx',
    # 'before': 'xxx',
    # 'limit': '100',
    # 'ordId': 'xxx'
}

res = trade_test.get_orders_history(params)