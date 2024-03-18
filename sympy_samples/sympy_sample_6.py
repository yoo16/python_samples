from sympy import *

a = 1
b = 2
c = -1
d = 1

x = Symbol('x')
y = Symbol('y')

func = a*x**3 + b*x**2 + c*x + d
print(func)

result = solve(func, x)
print(result)