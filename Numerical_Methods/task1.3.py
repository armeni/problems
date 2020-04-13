import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


def newton(f, x0, eps):
    x = Symbol('x')
    sym_f = parse_expr(f)
    f = lambdify(x, sym_f)
    df = lambdify(x, diff(sym_f, x))
    while True:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1

        
def newton_system(f1, f2, x0, y0, eps):
    x, y = symbols('x y')
    f1_sym, f2_sym = parse_expr(f1), parse_expr(f2)
    f1, f2 = lambdify((x, y), f1_sym), lambdify((x, y), f2_sym)
    df1dx = lambdify((x, y), diff(f1_sym, x))
    df2dx = lambdify((x, y), diff(f2_sym, x))
    df1dy = lambdify((x, y), diff(f1_sym, y))
    df2dy = lambdify((x, y), diff(f2_sym, y))
    while True:
        g, h = np.linalg.solve(
            np.array([
                [df1dx(x0, y0), df1dy(x0, y0)],
                [df2dx(x0, y0), df2dy(x0, y0)]
            ]),
            np.array([
                -f1(x0, y0),
                -f2(x0, y0)
            ]))
        x1, y1 = x0 + g, y0 + h
        if abs(x1 - x0) + abs(y1 - y0) < eps:
            return x1, y1
        x0, y0 = x1, y1

eps = 1e-4        
        
f = 'x**2 + 4 * sin(x) - 2'
x0 = 0
print('Root of equation:\nx = %f\n' % (newton(f, x0, eps)))

f1 = 'sin(y - 1) + x - 1.3'
f2 = 'y - sin(x + 1) - 0.8'
x0, y0 = 0, 0
print('Solution of system:\nx = %f\ny = %f' % (newton_system(f1, f2, x0, y0, eps)))