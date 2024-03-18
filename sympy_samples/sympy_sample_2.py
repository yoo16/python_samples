from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# 数式作成
a, b, c = 1, 2, -1
x, y = symbols('x, y')
y = a*x**2 + b*x + c

# 解
result = solve(y, x)
print(result)

# グラフプロット
x_data = np.arange(-10, 10, 0.1)
y_data = [y.subs(x, value) for value in x_data]
plt.plot(x_data, y_data)

# 解のプロット
for value in result:
    plt.scatter(value, 0)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()