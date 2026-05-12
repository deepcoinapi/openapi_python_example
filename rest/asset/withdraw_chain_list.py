from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'ccy': 'USDT',
}

res = asset_test.get_withdraw_chain_list(params)