import cv2

# カスケード分類器の読み込み
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade = cascade
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# カメラからの入力を開始
cap = cv2.VideoCapture(0)

while True:
    # フレームの読み込み
    ret, frame = cap.read()

    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顔検出の実行
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 検出された顔に矩形を描画
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 結果の表示
    cv2.imshow('Face Detection', frame)

    # 'q'キーが押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# リソースの解放
cap.release()
cv2.destroyAllWindows()