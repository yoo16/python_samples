import cv2
import numpy as np
import os

# 学習データの保存先ディレクトリ
train_dir = 'train_data'

# 画像サイズ
image_size = (100, 100)

# 顔検出のためのカスケード分類器
face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

# ラベル（人物ID）の入力
label = input("Enter label (person ID) for training: ")

# 学習データの保存先ディレクトリを作成
os.makedirs(os.path.join(train_dir, label), exist_ok=True)

# OpenCVの最適化を有効にする
cv2.setUseOptimized(True)

# カメラからの入力
cap = cv2.VideoCapture(cv2.CAP_ANY)

# カメラが正常に初期化されたかを確認
if not cap.isOpened():
    print("Error opening video capture")
    exit()

# 学習データの収集
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame")
        break

    # 顔検出
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # 顔領域の切り抜き
        face_roi = gray[y:y+h, x:x+w]
        face_roi = cv2.resize(face_roi, image_size)

        # 学習データの保存
        cv2.imwrite(os.path.join(train_dir, label, f"{count}.jpg"), face_roi)
        count += 1

        # 顔の周囲に矩形を描画
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Collecting Training Data", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 100枚の学習データを収集したら終了
    if count >= 100:
        break

cap.release()
cv2.destroyAllWindows()

# 学習データの読み込み
def load_train_data(directory):
    X_train = []
    y_train = []
    for subdir in os.listdir(directory):
        path = os.path.join(directory, subdir)
        if not os.path.isdir(path):
            continue
        for filename in os.listdir(path):
            img = cv2.imread(os.path.join(path, filename), cv2.IMREAD_GRAYSCALE)
            X_train.append(img)
            y_train.append(int(subdir))
    return X_train, y_train

# 分類器の学習
def train_recognizer(X_train, y_train):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(X_train, np.array(y_train))
    return recognizer

# 学習データの読み込み
X_train, y_train = load_train_data(train_dir)

# 分類器の学習
recognizer = train_recognizer(X_train, y_train)

# モデルの保存
recognizer.save('model/face_recognizer_model.yml')
print("Training completed and model saved.")