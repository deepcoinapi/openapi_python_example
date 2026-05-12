from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'orders': [
        {
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
            'sz': '1',
            'px': '60000',
            # 'reduceOnly': 'false',
            # 'tgtCcy': 'base_ccy',
            'tpTriggerPx': '100000',
            'slTriggerPx': '50000',
        },
        {
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
            'sz': '2',
            'px': '61000',
            # 'reduceOnly': 'false',
            # 'tgtCcy': 'base_ccy',
            'tpTriggerPx': '100000',
            'slTriggerPx': '50000',
        }
    ]

}

res = trade_test.post_batch_order(params)