from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instId': 'BTC-USDT-SWAP',
    'productGroup': 'Swap',
    'sz': '10',
    'side': 'buy',
    'posSide': 'long',
    'price': '80000',
    'isCrossMargin': '1',
    'orderType': 'limit',
    'triggerPrice': '88000',
    'triggerPxType': 'last',
    'mrgPosition': 'merge',
    # 'closePosId': 'xxx',
    'tdMode': 'cross',
    # 'tpTriggerPx': 'xxx',
    # 'tpTriggerPxType': 'last',
    # 'tpOrdPx': -1,
    # 'slTriggerPx': 'xxx',
    # 'slTriggerPxType': 'last',
    # 'slOrdPx': -1,
}

res = trade_test.post_trigger_order(params)