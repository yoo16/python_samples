import cv2 as cv
import os

# 現在の作業ディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
# 画像パス
image_path = os.path.join(current_dir, "images", "people_1.png")
# 画像読み込み
img = cv.imread(image_path)

if img is None:
    print("ファイルを読み込めませんでした。")
else:
    # 画像表示
    cv.imshow("people", img)
    # 何かキーが押されるまで待機
    cv.waitKey(0)