from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# x値の範囲を生成 (-3π から 3πまで)
min = -np.pi*3
max = np.pi*3

# 係数設定
a1 = 1
a2 = 1
b1 = 0
b2 = 0

# xを400サンプル生成
x_data = np.linspace(min, max, 400)

# データ計算
y1_data = a1 * np.sin(x_data) + b1
y2_data = a2 * np.cos(x_data) + b2

# 解
x = symbols('x')
eq = (a1 * sin(x) + b1) - (a2 * cos(x) + b2)
results = solveset(eq, x, domain=Interval(min, max))
print(results)

# グラフサイズ
plt.figure(figsize=(10, 4))

# グラフをプロット
plt.plot(x_data, y1_data, color="green")
plt.plot(x_data, y2_data, color="red")

# 解のプロット
for result in results:
    x_plot = result
    y_plot = a1 * sin(x_plot) + b1
    plt.scatter(x_plot, y_plot)

# タイトルと軸ラベルを追加
plt.xlabel('x')
plt.ylabel('y')

# 目盛り
x_ticks = np.arange(min, max + np.pi, np.pi)
x_tick_labels = [f"${s:.0f}\\pi$" if s != 0 else '0' for s in x_ticks / np.pi]
plt.xticks(x_ticks, x_tick_labels)

# グリッドを表示
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()