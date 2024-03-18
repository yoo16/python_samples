from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# シンボルの定義
x, y = symbols('x y')

# 係数の定義
a1 = 2
b1 = 1
a2 = -1
b2 = 4

# 方程式の定義
eq1 = y - a1*x - b1
eq2 = y - a2*x - b2

# 連立方程式の解
result = solve((eq1, eq2))
print(result)

# グラフプロット
x_data = np.linspace(-10, 10, 100)
y1_data = a1*x_data + b1
y2_data = a2*x_data + b2

# グラフ描画
plt.plot(x_data, y1_data, label=f"y = {a1}x + {b1}")
plt.plot(x_data, y2_data, label=f"y = {a2}x + {b2}")

plt.scatter(result[x], result[y], color="red")

label = f"({result[x]}, {result[y]})"
plt.annotate(label, (result[x], result[y]))

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()