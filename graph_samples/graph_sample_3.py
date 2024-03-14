import matplotlib.pyplot as plt

# 始点
x1, y1 = 0, 0
# ベクトル
v1, w1 = 4, 2
v2, w2 = 2, 2

plt.quiver(x1, y1, v1, w1, color='red', angles='xy', scale_units='xy', scale=1)
plt.quiver(v1, w1, v2, w2, color='green', angles='xy', scale_units='xy', scale=1)
plt.xlim([0,10])
plt.ylim([0,10])
plt.grid()
plt.show()