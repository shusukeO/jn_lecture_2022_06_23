# ライブラリのインポート(open cvをプログラムに導入する）
import base64
import cv2
# 前回のbekku様が紹介された通信をするためのライブラリのインポート
import socket

# # open cvを使ってみる
# # cv2.〇〇で使える（今回はversionを返すだけ）
# print(cv2.__version__)

# カメラを設定
cap = cv2.VideoCapture(0)

# frame変数をグローバルで使えるようにする
frame = ""

# 連続でカメラから値を取得するためにループ
while True:
    # カメラからの画像取得
    ret, frame = cap.read()

    # カメラの画像の出力
    cv2.imshow('camera', frame)

    # 「sキー」で、写真を撮って、ループから抜ける
    key = cv2.waitKey(10)
    if key == ord('s'):
        cv2.imwrite('pic.jpeg', frame)
        break

# メモリを解放して終了する
cap.release()
cv2.destroyAllWindows()
# ウインドウが閉じれないバグ対応
cv2.waitKey(1)


# 写真をバイトデータに変換する
ret, dst_data = cv2.imencode('.jpeg', frame)
dst_str = base64.b64encode(dst_data)

# グローバル変数
PORT = 50000      # ポート番号

# メイン実行部
# ソケットの作成
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# アドレスの設定
server.bind(("", PORT))
# 接続の待ち受け
server.listen()

# クライアントへの対応処理
while True:                                    # 対応の繰り返し
    client, addr = server.accept()             # 通信用ソケットの取得
    print("接続要求あり")
    print(client)
    client.sendall(dst_str)        # メッセージの送信
    client.close()
