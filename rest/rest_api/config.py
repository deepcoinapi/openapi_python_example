def api_key():
    #todo:use your real api_key
    params = {}
    params['__api_key'] = 'your apikey'
    params['__secret_key'] = 'your secretkey'
    params['__passphrase'] = 'your passphrase'

    params['host'] = 'https://api.deepcoin.com'
    return params
