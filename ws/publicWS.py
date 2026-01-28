import websocket
import json
import time
import threading

# ws_url = "wss://stream.deepcoin.com/streamlet/trade/public/spot?platform=api" # 現貨
ws_url = "wss://stream.deepcoin.com/streamlet/trade/public/swap?platform=api" # 合約

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
            time.sleep(30)

    threading.Thread(target=send_heartbeat, daemon=True).start()

    ### 最新行情
    # request_data = {
    #     "SendTopicAction": {
    #         "Action": "1",
    #         "FilterValue": "DeepCoin_ETHUSDT",
    #         "LocalNo": 111,
    #         "ResumeNo": -2,
    #         "TopicID": "7"
    #     }
    # }
    ### 最近成交
    request_data = {
        "SendTopicAction": {
            "Action": "1",
            "FilterValue": "DeepCoin_ETHUSDT",
            "LocalNo": 111,
            "ResumeNo": -2,
            "TopicID": "2"
        }
    }
    ### K線（僅支持一分鐘）
    # request_data = {
    #     "SendTopicAction": {
    #         "Action": "1",
    #         "FilterValue": "DeepCoin_BTCUSDT_1m",
    #         "LocalNo": 6,
    #         "ResumeNo": -1,
    #         "TopicID": "11"
    #         }
    # }
    ### 25檔增量行情
    # request_data = {
    #     "SendTopicAction": {
    #         "Action": "1",
    #         "FilterValue": "DeepCoin_ETHUSDT_0.01",
    #         "LocalNo": 111,
    #         "ResumeNo": -1,
    #         "TopicID": "25"
    #     }
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