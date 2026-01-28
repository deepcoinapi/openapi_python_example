from rest.utils.request_util import BaseMethod
from rest.rest_api.config import api_key
import requests

class MarketTest(object):
    def __init__(self):
        self.host = api_key()['host']

    def get_orderbook(self, params, uri='/deepcoin/market/books'):
        """ 獲取產品深度列表
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/marketBooks
        GET /deepcoin/market/books
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_kline(self, params, uri='/deepcoin/market/candles'):
        """ 獲取交易產品 K 線數據
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getKlineData
        GET /deepcoin/market/candles
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_instruments(self, params, uri='/deepcoin/market/instruments'):
        """ 獲取交易產品基礎信息
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getBaseInfo
        GET /deepcoin/market/instruments
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_tickers(self, params, uri='/deepcoin/market/tickers'):
        """ 獲取所有產品行情信息
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getMarketTickers
        GET /deepcoin/market/tickers
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_index_kline(self, params, uri='/deepcoin/market/index-candles'):
        """ 獲取交易產品指數 K 線數據
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getIndexKlineData
        GET /deepcoin/market/index-candles
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_trades(self, params, uri='/deepcoin/market/trades'):
        """ 獲取交易產品指數 K 線數據
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getTrades
        GET /deepcoin/market/trades
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_mark_kline(self, params, uri='/deepcoin/market/mark-price-candles'):
        """ 獲取交易產品指數 K 線數據
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getMarkKlineData
        GET /deepcoin/market/mark-price-candles
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_step_margin(self, params, uri='/deepcoin/market/step-margin'):
        """ 獲取交易產品指數 K 線數據
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getStepMargin
        GET /deepcoin/market/step-margin
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_book_spread(self, params, uri='/deepcoin/market/book-spread'):
        """ 獲取交易產品指數 K 線數據
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/getBookSpread
        GET /deepcoin/market/book-spread
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url, params=params)
        print(f"resp:{res.json()}")
        return res.json()

    def get_time(self, uri='/deepcoin/market/time'):
        """ 獲取交易產品指數 K 線數據
        https://www.deepcoin.com/docs/zh/DeepCoinMarket/systemInfo
        GET /deepcoin/market/time
        """
        url = '{}{}'.format(self.host, uri)
        res = requests.request('GET', url)
        print(f"resp:{res.json()}")
        return res.json()

class AccountTest(object):
    def __init__(self):
        self.__api_key = api_key()['__api_key']
        self.__secret_key = api_key()['__secret_key']
        self.__passphrase = api_key()['__passphrase']
        self.host = api_key()['host']

    def get_listenkey(self, uri='/deepcoin/listenkey/acquire'):
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def extend_listenkey(self, uri='/deepcoin/listenkey/extend'):
        params = {}
        params['listenkey'] = 'xxx'
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_account_balance(self, params, uri='/deepcoin/account/balances'):
        """ 獲取資金帳戶餘額
        https://www.deepcoin.com/docs/zh/DeepCoinAccount/getAccountBalance
        GET /deepcoin/account/balances
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_account_bills(self, params, uri='/deepcoin/account/bills'):
        """ 獲取資金流水
        https://www.deepcoin.com/docs/zh/DeepCoinAccount/getAccountBills
        GET /deepcoin/account/bills
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_account_positions(self, params, uri='/deepcoin/account/positions'):
        """ 獲取持倉列表
        https://www.deepcoin.com/docs/zh/DeepCoinAccount/accountPositions
        GET /deepcoin/account/positions
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    # 設置槓桿倍數
    def post_set_leverage(self, params, uri='/deepcoin/account/set-leverage'):
        """
        https://www.deepcoin.com/docs/zh/DeepCoinAccount/accountSetLeverage
        POST /deepcoin/account/set-leverage
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

class TradeTest(object):
    def __init__(self):
            self.__api_key = api_key()['__api_key']
            self.__secret_key = api_key()['__secret_key']
            self.__passphrase = api_key()['__passphrase']
            self.host = api_key()['host']

    def post_order(self, params, uri='/deepcoin/trade/order'):
        """ 下單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/order
        POST /deepcoin/trade/order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    # 撤單
    def cancel_order(self, params, uri='/deepcoin/trade/cancel-order'):
        """ 撤單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/cancelOrder
        POST /deepcoin/trade/cancel-order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def replace_order(self, params, uri='/deepcoin/trade/replace-order'):
        """ 改單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/replaceOrder
        POST /deepcoin/trade/replace-order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    # 批量撤單
    def batch_cancel_order(self, params, uri='/deepcoin/trade/batch-cancel-order'):
        """ 批量撤單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/batchCancelOrder
        POST /deepcoin/trade/batch-cancel-order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    # 撤銷條件單
    def cancel_trigger_order(self, params, uri='/deepcoin/trade/cancel-trigger-order'):
        """ 撤銷條件單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/cancelTriggerOrder
        POST /deepcoin/trade/cancel-trigger-order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    # 一鍵撤單
    def cancel_all_orders(self, params, uri='/deepcoin/trade/swap/cancel-all'):
        """ 一鍵撤單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/cancelAllOrder
        POST /deepcoin/trade/swap/cancel-all
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def get_trade_fills(self, params, uri='/deepcoin/trade/fills'):
        """ 獲取成交明細
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/tradeFills
        GET /deepcoin/trade/fills
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_orderByID(self, params, uri='/deepcoin/trade/orderByID'):
        """ 根據id獲取指定委託信息
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/orderByID
        GET /deepcoin/trade/orderByID
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_finishOrderByID(self, params, uri='/deepcoin/trade/finishOrderByID'):
        """ 根據id獲取指定歷史委託信息
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/finishOrderByID
        GET /deepcoin/trade/finishOrderByID
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_orders_history(self, params, uri='/deepcoin/trade/orders-history'):
        """ 獲取歷史訂單紀錄
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/ordersHistory
        GET /deepcoin/trade/orders-history
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_orders_pending(self, params, uri='/deepcoin/trade/v2/orders-pending'):
        """ 獲取未成交訂單列表
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/ordersPendingV2
        GET /deepcoin/trade/v2/orders-pending
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_funding_rate(self, params, uri='/deepcoin/trade/funding-rate'):
        """ 獲取資金費率結算周期
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/fundingRate
        GET /deepcoin/trade/funding-rate
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def post_trigger_order(self, params, uri='/deepcoin/trade/trigger-order'):
        """ 條件單下單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/triggerOrder
        POST /deepcoin/trade/trigger-order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def batch_close_position(self, params, uri='/deepcoin/trade/batch-close-position'):
        """ 批量平倉
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/batchClosePosition
        POST /deepcoin/trade/batch-close-position
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def get_current_funding_rate(self, params, uri='/deepcoin/trade/fund-rate/current-funding-rate'):
        """ 當前資金費率
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/currentFundRate
        GET /deepcoin/trade/fund-rate/current-funding-rate
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def get_history_funding_rate(self, params, uri='/deepcoin/trade/fund-rate/history'):
        """ 歷史資金費率
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/fundingRateHistory
        GET /deepcoin/trade/fund-rate/history
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def replace_order_sltp(self, params, uri='/deepcoin/trade/replace-order-sltp'):
        """ 修改開倉限價單止盈止損
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/replaceTPSL
        POST /deepcoin/trade/replace-order-sltp
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def close_position_by_ids(self, params, uri='/deepcoin/trade/close-position-by-ids'):
        """ 按倉位 ID 平倉
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/closePositionByIds
        POST /deepcoin/trade/close-position-by-ids
        """

        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def set_position_sltp(self, params, uri='/deepcoin/trade/set-position-sltp'):
        """ 設置持倉止盈止損
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/setPositionSlTp
        POST /deepcoin/trade/set-position-sltp
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def modify_position_sltp(self, params, uri='/deepcoin/trade/modify-position-sltp'):
        """ 修改持倉止盈止損
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/modifyPositionSlTp
        POST /deepcoin/trade/modify-position-sltp
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def cancel_position_sltp(self, params, uri='/deepcoin/trade/cancel-position-sltp'):
        """ 取消持倉止盈止損
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/cancelPositionSlTp
        POST /deepcoin/trade/cancel-position-sltp
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def trigger_orders_pending(self, params, uri='/deepcoin/trade/trigger-orders-pending'):
        """ 查詢未觸發條件單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/triggerOrdersPending
        GET /deepcoin/trade/trigger-orders-pending
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def trigger_orders_history(self, params, uri='/deepcoin/trade/trigger-orders-history'):
        """ 查詢已觸發條件單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/triggerOrdersHistory
        GET /deepcoin/trade/trigger-orders-history
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def trace_order(self, params, uri='/deepcoin/trade/trace-order'):
        """ 追蹤出場委託單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/traceOrder#%E8%BF%BD%E8%B8%AA%E5%87%BA%E5%9C%BA%E5%A7%94%E6%89%98%E5%8D%95
        POST /deepcoin/trade/trace-order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def trace_order_list(self, params, uri='/deepcoin/trade/trace-order-list'):
        """ 查詢追蹤出場委託單
        https://www.deepcoin.com/docs/zh/DeepCoinTrade/traceOrder#%E6%9F%A5%E7%9C%8B%E8%BF%BD%E8%B8%AA%E5%87%BA%E5%9C%BA%E5%A7%94%E6%89%98%E5%8D%95
        GET /deepcoin/trade/trace-order-list
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

class CopyTradingTest(object):
    def __init__(self):
        self.__api_key = api_key()['__api_key']
        self.__secret_key = api_key()['__secret_key']
        self.__passphrase = api_key()['__passphrase']
        self.host = api_key()['host']

    def leader_settings(self, params, uri='/deepcoin/copytrading/leader-settings'):
        """ 帶單設置
        https://www.deepcoin.com/docs/zh/copyTrade/copyTradingList
        POST /deepcoin/copytrading/leader-settings
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def support_contracts(self, uri='/deepcoin/copytrading/support-contracts'):
        """ 獲取帶單合約
        https://www.deepcoin.com/docs/zh/copyTrade/getSupportContract
        GET /deepcoin/copytrading/support-contracts
        """
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def set_contracts(self, params, uri='/deepcoin/copytrading/set-contracts'):
        """ 設置帶單合約
        https://www.deepcoin.com/docs/zh/copyTrade/settingCopyTradingContract
        POST /deepcoin/copytrading/set-contracts
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def leader_position(self, uri='/deepcoin/copytrading/leader-position'):
        """ 帶單者倉位
        https://www.deepcoin.com/docs/zh/copyTrade/getPosition
        GET /deepcoin/copytrading/leader-position
        """
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def estimate_profit(self, uri='/deepcoin/copytrading/estimate-profit'):
        """ 帶單者分潤
        https://www.deepcoin.com/docs/zh/copyTrade/getEstimatedProfit
        GET /deepcoin/copytrading/estimate-profit
        """
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def history_profit(self, uri='/deepcoin/copytrading/history-profit'):
        """ 歷史分潤
        https://www.deepcoin.com/docs/zh/copyTrade/getHistoryProfit
        GET /deepcoin/copytrading/history-profit
        """
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def follower_rank(self, params, uri='/deepcoin/copytrading/follower-rank'):
        """ 跟單者列表
        https://www.deepcoin.com/docs/zh/copyTrade/followerList
        GET /deepcoin/copytrading/follower-rank
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def position_type(self, uri='/deepcoin/copytrading/position-type'):
        """ 獲取倉位模式
        https://www.deepcoin.com/docs/zh/copyTrade/positionType
        GET /deepcoin/copytrading/position-type
        """
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def post_position_type(self, params, uri='/deepcoin/copytrading/position-type'):
        """ 更新倉位模式
        https://www.deepcoin.com/docs/zh/copyTrade/positionType#%E6%9B%B4%E6%96%B0%E4%BB%93%E4%BD%8D%E6%A8%A1%E5%BC%8F
        POST /deepcoin/copytrading/position-type
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

class AssetTest(object):
    def __init__(self):
        self.__api_key = api_key()['__api_key']
        self.__secret_key = api_key()['__secret_key']
        self.__passphrase = api_key()['__passphrase']
        self.host = api_key()['host']

    def internal_transfer_support(self, uri='/deepcoin/internal-transfer/support'):
        """ 獲取劃轉幣種
        https://www.deepcoin.com/docs/zh/InternalTransfer/getSupportCoin
        GET /deepcoin/internal-transfer/support
        """
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def internal_transfer(self, params, uri='/deepcoin/internal-transfer'):
        """ 內部劃轉
        https://www.deepcoin.com/docs/zh/InternalTransfer/goInternalTransfer
        POST /deepcoin/internal-transfer
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def internal_transfer_history(self, params, uri='/deepcoin/internal-transfer/history-order'):
        """ 內部劃轉歷史
        https://www.deepcoin.com/docs/zh/InternalTransfer/internalTransferHistory
        GET /deepcoin/internal-transfer/history-order
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def deposit_list(self, params, uri='/deepcoin/asset/deposit-list'):
        """ 獲取充值紀錄
        https://www.deepcoin.com/docs/zh/assets/deposit
        GET /deepcoin/asset/deposit-list
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def withdraw_list(self, params, uri='/deepcoin/asset/withdraw-list'):
        """ 獲取提現紀錄
        https://www.deepcoin.com/docs/zh/assets/withdraw
        GET /deepcoin/asset/withdraw-list
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    # 查詢充值鏈列表
    def get_recharge_chain_list(self, params, uri='/deepcoin/asset/recharge-chain-list'):
        """ 查詢充值鏈列表
        https://www.deepcoin.com/docs/zh/assets/chainlist
        GET /deepcoin/asset/recharge-chain-list
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def asset_transfer(self, params, uri='/deepcoin/asset/transfer'):
        """ 資金劃轉
        https://www.deepcoin.com/docs/zh/assets/transfer
        POST /deepcoin/asset/transfer
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

class SubAccountTest(object):
    def __init__(self):
        self.__api_key = api_key()['__api_key']
        self.__secret_key = api_key()['__secret_key']
        self.__passphrase = api_key()['__passphrase']
        self.host = api_key()['host']

    def sub_account_transfer(self, params, uri='/deepcoin/sub-account/sub-account-transfer'):
        """ 母子帳戶劃轉
        https://www.deepcoin.com/docs/zh/SubAccount/transfer
        POST /deepcoin/sub-account/sub-account-transfer
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def sub_account_transfer_record(self, params, uri='/deepcoin/sub-account/sub-account-transfer-record'):
        """ 母子帳戶劃轉紀錄
        https://www.deepcoin.com/docs/zh/SubAccount/transferRecord
        GET /deepcoin/sub-account/sub-account-transfer-record
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def sub_account_list(self, uri='/deepcoin/sub-account/sub-account-list'):
        """ 查詢子帳號列表
        https://www.deepcoin.com/docs/zh/SubAccount/subAccountList
        GET /deepcoin/sub-account/sub-account-list
        """
        params = {}
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

class RebateTest(object):
    def __init__(self):
        self.__api_key = api_key()['__api_key']
        self.__secret_key = api_key()['__secret_key']
        self.__passphrase = api_key()['__passphrase']
        self.host = api_key()['host']

    def rebate_rate(self, params, uri='/deepcoin/rebate/config'):
        """ 返佣比例查詢
        https://www.deepcoin.com/docs/zh/rebate/rateInquiry
        GET /deepcoin/rebate/config
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def rebate_config(self, params, uri='/deepcoin/rebate/config'):
        """ 返佣比例設置
        https://www.deepcoin.com/docs/zh/rebate/rateSetting
        POST /deepcoin/rebate/config
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'POST')
        r = handler.request_app(params)
        return r

    def agents_users(self, params, uri='/deepcoin/agents/users'):
        """ 合夥人查詢
        https://www.deepcoin.com/docs/zh/rebate/affiliates
        GET /deepcoin/agents/users
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def rebate_list(self, params, uri='/deepcoin/agents/users/rebate-list'):
        """ 返佣明細查詢
        https://www.deepcoin.com/docs/zh/rebate/history
        GET /deepcoin/agents/users/rebate-list
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

    def rebate_total(self, params, uri='/deepcoin/agents/users/rebates'):
        """ 返佣匯總查詢
        https://www.deepcoin.com/docs/zh/rebate/summary
        GET /deepcoin/agents/users/rebates
        """
        handler = BaseMethod(self.__api_key, self.__secret_key, self.__passphrase, self.host, uri, 'GET')
        r = handler.request_app(params)
        return r

