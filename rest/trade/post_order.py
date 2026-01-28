from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'tdMode': 'cross',
    # 'ccy': 'USDT',
    # 'clOrdId': 'test',
    # 'tag': 'TEST',
    'side': 'buy',
    'posSide': 'long',
    'mrgPosition': 'merge',
    # 'closePosId': '',
    'ordType': 'limit',
    'sz': '10',
    'px': '85000',
    # 'reduceOnly': 'false',
    'tgtCcy': 'base_ccy',
    'tpTriggerPx': '100000',
    'slTriggerPx': '80000',
}

res = trade_test.post_order(params)