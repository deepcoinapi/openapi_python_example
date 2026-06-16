import websocket
import json
import time
import threading

# ws_url = "wss://stream.deepcoin.com/streamlet/trade/public/spot?platform=api&version=v2" # 現貨
ws_url = "wss://stream.deepcoin.com/streamlet/trade/public/swap?platform=api&version=v2" # 合約

# ws_url = "wss://stream.deepcoin.com/v1/private" + "?listenKey=" + 'xxx'

def on_message(ws, message):
    print(f"Received: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")


def on_open(ws):
    print("WebSocket connected")


    def send_heartbeat():
        while True:
            ws.send("ping")
            print("Sent: ping")
            time.sleep(10)

    threading.Thread(target=send_heartbeat, daemon=True).start()

    ### 最新行情
    request_data = {
      "Action": "1",
      "Symbol": "BTCUSDT",
      "LocalNo": 6,
      "ResumeNo": -1,
      "Topic": "market"
    }

    ### 最近成交
    # request_data = {
    #   "Action": "1",
    #   "Symbol": "BTCUSDT",
    #   "LocalNo": 6,
    #   "ResumeNo": -1,
    #   "Topic": "trade"
    # }

    ### K線
    # request_data = {
    #   "Action": "1",
    #   "Symbol": "BTCUSDT",
    #   "LocalNo": 6,
    #   "Count": 10,        # 请求历史数据条数，最大为100
    #   "Topic": "kline",
    #   "PeriodID": "4h"    # 周期
    # }

    ### 25檔增量行情
    # request_data = {
    #   "Action": "1",
    #   "Symbol": "BTCUSDT",
    #   "LocalNo": 6,
    #   "ResumeNo": -1,
    #   "Topic": "book25"
    # }

    ### 強平訂單
    # request_data = {
    #   "Action": "1",
    #   "LocalNo": 0,
    #   "Topic": "liquidationOrder"
    # }

    ws.send(json.dumps(request_data))
    print(f"Sent: {json.dumps(request_data)}")


ws = websocket.WebSocketApp(
    ws_url,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)

ws.run_forever()