from rest.rest_api import deepcoin_api

rebate_test = deepcoin_api.RebateTest()

params = {
    'uid': 'xxx',
    'type': 2,
    'startTime': 'xxx',
    'endtime': 'xxx'
}

res = rebate_test.rebate_total(params)