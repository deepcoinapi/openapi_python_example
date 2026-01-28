from rest.rest_api import deepcoin_api

market_test = deepcoin_api.MarketTest()

res = market_test.get_time()
