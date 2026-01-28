from rest.rest_api import deepcoin_api

rebate_test = deepcoin_api.RebateTest()

params = {
    'uid': 'xxx',
    'rate': '20'
}

res = rebate_test.rebate_config(params)