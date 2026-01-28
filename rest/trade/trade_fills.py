from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instType': 'SWAP',
    'instId': 'BTC-USDT-SWAP',
    # 'ordId': 'xxx',
    # 'after': 'xxx',
    # 'before': 'xxx',
    # 'begin': 'xxx',
    # 'end': 'xxx',
    'limit': '100'
}

res = trade_test.get_trade_fills(params)