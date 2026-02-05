# DeepCoin OpenAPI Python Example

Python 版本的 DeepCoin OpenAPI 示例代碼，包含REST API 和 WebSocket API 的實現。
## 參考文檔

- API文檔: https://www.deepcoin.com/docs/zh/authentication

## 使用說明
## REST API 示例

請先於 `rest/rest_api/config.py`中填入對應的 apikey、secretkey 和 passphrase

打開 `rest` 目錄，參考各個接口使用對應的API。

### Python Example
`rest/rest_api/account/account_balance.py`
```python
from rest.rest_api import deepcoin_api

account_test = deepcoin_api.AccountTest()

params = {
    'instType': 'SWAP',
    'ccy': 'USDT'
}

res = account_test.get_account_balance(params)
```

## WebSocket 示例

#### 公有WebSocket（訂閱最新行情）

### Python Example
`ws/publicWS.py`
```python
import websocket
import json
import time
import threading

ws_url = "wss://stream.deepcoin.com/streamlet/trade/public/swap?platform=api"

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
    request_data = {
        "SendTopicAction": {
            "Action": "1",
            "FilterValue": "DeepCoin_ETHUSDT",
            "LocalNo": 111,
            "ResumeNo": -2,
            "TopicID": "7"
        }
    }

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
```
