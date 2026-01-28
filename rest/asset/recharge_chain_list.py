from rest.rest_api import deepcoin_api

asset_test = deepcoin_api.AssetTest()

params = {
    'currency_id': 'USDT',
    'lang': 'zh'
}

res = asset_test.get_recharge_chain_list(params)