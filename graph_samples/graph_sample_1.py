import matplotlib.pyplot as plt

x = [-3, -1, 2, 4]
y = [-2, 1, 3, 2]

print(x)
print(y)

# プロット
plt.plot(x, y)
plt.scatter(x, y)

# X, Y軸ラベル
plt.xlabel('X')
plt.ylabel('Y')

# 軸範囲
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# 目盛り
plt.xticks(range(-10, 11, 2))
plt.yticks(range(-10, 11, 2))

# ゼロ線
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
# グリッド線
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
# グラフ描画
plt.show()