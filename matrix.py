import numpy as np

vector = np.arange(1, 6)
print(vector)

vector += 2
print(vector)

vector *= 2
print(vector)

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
print("---2次元配列---")
print(vector1)
print(vector2)

# 足し算
result = vector1 + vector2 
print("---足し算---")
print(result)

# 掛け算
result = vector1 * vector2
print("---掛け算---")
print(result)


# zero()
zeros = np.zeros((5), dtype=int)
print(zeros)

zeros = np.zeros((2, 3))
print(zeros)

# complex_array = np.zeros((2, 3), dtype=complex)
# print(complex_array)

# 結合
# 2次元配列の結合
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8, 9], [10, 11, 12]])

print("---2つの行列---")
print(matrix1)
print(matrix2)

matrix3 = np.concatenate((matrix1, matrix2))
print(matrix3.shape)
print(matrix3)
print(matrix3[2][0])

matrix4 = np.concatenate((matrix1, matrix2), axis=1)
print(matrix4.shape)
print(matrix4)
print(matrix4[0][3])

## reshape
## 2 x 3
matrix5 = np.array([[1, 2, 3], [4, 5, 6]])
new_matrix = matrix5.reshape(3, 2)
print(matrix1.shape)
print(matrix1)

print(new_matrix.shape)
print(new_matrix)

matrix6 = np.array([[1, 2, 3], [4, 5, 6]])
new_matrix = matrix6.reshape(1, 6)
print(new_matrix.shape)
print(new_matrix)


# vector3 = np.array([1, 2, 3, 4, 5])
# vector4 = vector3[1:4]
# print(vector4)