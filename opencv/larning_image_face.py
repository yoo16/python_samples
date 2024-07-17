import cv2 as cv
import numpy as np
import os

# 学習データのディレクトリ
train_dir = 'train_data'

# 画像サイズ
image_size = (100, 100)

# 学習データの読み込み
def load_train_data(directory):
    X_train = []
    y_train = []
    for subdir in os.listdir(directory):
        path = os.path.join(directory, subdir)
        if not os.path.isdir(path):
            continue
        for filename in os.listdir(path):
            try:
                img = cv.imread(os.path.join(path, filename), cv.IMREAD_GRAYSCALE)
                img = cv.resize(img, image_size)
                X_train.append(img)
                y_train.append(int(subdir))
            except Exception as e:
                print(f"Error loading image: {filename}")
                print(str(e))
    return X_train, y_train

# 分類器の学習
def train_recognizer(X_train, y_train):
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.train(X_train, np.array(y_train))
    return recognizer

# 顔の認識
def recognize_face(recognizer, img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    label, confidence = recognizer.predict(gray)
    return label, confidence

# 学習データの読み込み
X_train, y_train = load_train_data(train_dir)

# 分類器の学習
recognizer = train_recognizer(X_train, y_train)

# カメラからの入力
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 顔の認識
    label, confidence = recognize_face(recognizer, frame)

    # 認識結果の表示
    cv.putText(frame, f"Label: {label}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.putText(frame, f"Confidence: {confidence}", (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow("Face Recognition", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()