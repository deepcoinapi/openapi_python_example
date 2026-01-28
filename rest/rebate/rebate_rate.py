from rest.rest_api import deepcoin_api

rebate_test = deepcoin_api.RebateTest()

params = {
    'uid': 'xxx',
    'startTime': 'xxx',
    'endTime': 'xxx'
}

res = rebate_test.rebate_rate(params)