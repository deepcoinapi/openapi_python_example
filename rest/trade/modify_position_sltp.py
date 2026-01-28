from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'instType': 'SWAP',
    'instId': 'BTC-USDT-SWAP',
    'ordId': '1001119776118867',
    'posSide': 'long',
    'mrgPosition': 'merge',
    'tdMode': 'cross',
    # 'posId': 'xxx', # 当 mrgPosition 为 split 时必填
    'tpTriggerPx': '99100',
    'tpTriggerPxType': 'last',
    'tpOrdPx': -1,
    'slTriggerPx': '80100',
    'slTriggerPxType': 'last',
    'slOrdPx': -1,
    'sz': '10' # 用於部分止盈止損，不填表示全部持倉
}

res = trade_test.modify_position_sltp(params)