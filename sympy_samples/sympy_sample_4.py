from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# 数式作成
a1, b1, c1 = 1, 2, -1
a2, b2 = 2, 1
x, y1, y2 = symbols('x, y1, y2')
y1 = a1*x**2 + b1*x + c1
y2 = a2*x + b2

# 解
result = solve(y1 - y2, x)
print(result)

# グラフプロット
x_data = np.arange(-10, 10, 0.1)
y1_data = [y1.subs(x, value) for value in x_data]
y2_data = [y2.subs(x, value) for value in x_data]
plt.plot(x_data, y1_data)
plt.plot(x_data, y2_data)

# 解のプロット
for x_value in result:
    y_value = a2*x_value + b2
    plt.scatter(x_value, y_value)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
