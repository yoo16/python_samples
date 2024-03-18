from sympy import symbols, sin, cos, solve, pi, pprint

# 変数の定義
x, n = symbols('x n')

# 方程式 sin(x) - cos(x) = 0 の基本解
solution = solve(sin(x) - cos(x), x)

# n の範囲を定義 (-2 から 2)
n_values = range(-2, 3)

# 解の計算と表示
print("解の例:")
for n_val in n_values:
    # 一般解の計算: n*pi + pi/4
    general_solution_1 = n_val*pi + solution[0]
    # 一般解の計算: n*pi + pi/4 - pi (これは -3*pi/4 に相当)
    general_solution_2 = n_val*pi + solution[0] - pi
    
    # 解の表示
    print(f"n = {n_val}:")
    pprint(general_solution_1, use_unicode=True)
    pprint(general_solution_2, use_unicode=True)
