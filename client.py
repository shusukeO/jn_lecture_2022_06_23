# モジュールのインポート
import socket

# open cvのインポート
import cv2

# 追加でモジュールのインポート
import base64
import numpy as np


# グローバル変数
HOST = "localhost"  # 接続先ホストの名前
# HOST = "127.0.0.1" # 接続先ホストの名前
PORT = 50000        # ポート番号

# 画像を受け取るので大きめに確保
BUFSIZE = 1000000      # 受信バッファの大きさ


# メイン実行部
# ソケットの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバとの接続
client.connect((HOST, PORT))

# サーバからのメッセージの受信
all_data = ''
data = ''
while True:
    data = client.recv(BUFSIZE)
    if not data:
        break
    else:
        all_data += data.decode("UTF-8")
print(len(all_data))


# data = client.recv(BUFSIZE)

# コネクションのクローズ
client.close()

# 写真データの形式の変換
img_data = base64.b64decode(all_data)
img_np = np.frombuffer(img_data, np.uint8)
src = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)


while True:
    cv2.imshow('pic', src)
    key = cv2.waitKey(100)

    # escキーでウインドウを閉じる
    if(int(key) == 27):
        break

cv2.destroyAllWindows()
