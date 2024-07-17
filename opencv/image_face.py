import cv2 as cv
import os

# 現在のフォルダ
current_dir = os.path.dirname(os.path.abspath(__file__))
# 画像パス
image_path = os.path.join(current_dir, "images/people_1.png")
# 画像読み込み
image = cv.imread(image_path)
# グレースケール変換
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# モデルファイルパス
model_path = os.path.join(
    current_dir, "data/haarcascades/haarcascade_frontalface_alt.xml")
# カスケード分類読み込み
face_cascade = cv.CascadeClassifier(model_path)

# 顔検出
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 検出した顔に矩形を描画
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 結果を表示
while True:
    # 画像表示
    cv.imshow('Face Detection', image)
    # escキーで終了
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
