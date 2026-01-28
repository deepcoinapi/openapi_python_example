from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

params = {
    'instType': 'SWAP',
    'uly': '',
}

res = market_test.get_tickers(params)