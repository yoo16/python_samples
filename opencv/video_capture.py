import cv2 as cv
import os

MAX_SIZE = 1000
def resizeFrame(frame):
    scale = 1.0
    # フレームの幅、高さ取得
    width = frame.shape[1]
    height = frame.shape[0]
    
    if ((width > height) and width > MAX_SIZE):
        # 幅が超えた場合
        scale = MAX_SIZE / width
    elif ((height > width) and height > MAX_SIZE):
        # 高さが超えた場合
        scale = MAX_SIZE / height

    # 再計算
    width = int(width * scale)
    height = int(height * scale)

    resize = (width, height)
    # リサイズ
    return cv.resize(frame, resize, interpolation=cv.INTER_AREA)

# 現在の作業ディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
# 画像パス
image_path = os.path.join(current_dir, "videos", "python_capture_video.mp4")
# 動画読み込み
capture = cv.VideoCapture(image_path)

if capture is None:
    print("ファイルを読み込めませんでした。")
else:
    while True:
        isTrue, frame = capture.read()
        # フレーム表示
        cv.imshow("Video", resizeFrame(frame))
        # 20ミリ秒間キー入力を待機し、Escキーが押されると終了
        if cv.waitKey(20) & 0xFF == 27:
            break

# キャプチャー終了
capture.release()
cv.destroyAllWindows()
