import numpy as np
import matplotlib.pyplot as plt

# 係数
a1, a2 = 2, -2
b1, b2 = 1, 5

# xの連続データ
x = np.linspace(-10, 10, 100)
print(x)

# Yの連続データ
y1 = a1 * x + b1
y2 = a2 * x + b2

print(y1)
print(y2)

# グラフ表示
plt.plot(x, y1, label=f"y = {a1}x + {b1}")
plt.plot(x, y2, label=f"y = {a2}x + {b2}")

# 係数行列
A = np.array([[a1, -1], [a2, -1]]) 

# 定数ベクトル
b = np.array([-b1, -b2])

print(A)
print(b)

# 方程式の解
point = np.linalg.solve(A, b)
print("(x, y)", point[0], point[1])

# 解のプロット
plt.scatter(point[0], point[1], color='red')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()