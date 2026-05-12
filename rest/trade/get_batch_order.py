from rest.rest_api import deepcoin_api

trade_test = deepcoin_api.TradeTest()

params = {
    'orders': [
        {
            'instId': 'BTC-USDT-SWAP',
            'ordId': '1000597586292096'
        },
        {
            'instId': 'BTC-USDT-SWAP',
            'ordId': '1000597586292097'
        }
    ]
}

res = trade_test.get_batch_orders(params)