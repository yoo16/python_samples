from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# シンボルの定義
x, y, z = symbols('x y z')

expr = (x + y)**2
print(expr)

expanded = expand((x + y)**2)
print(expanded)