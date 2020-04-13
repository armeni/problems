import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def f(x):
    return x - np.sin(x) - 0.25


def h(x):
    return np.abs(x) * (x - np.sin(x) - 0.25)


def lagrange(X, Y):
    x = symbols('x')
    L = 0
    for j in range(np.prod(X.shape)):
        l_num = 1
        l_denum = 1
        for i in range(np.prod(X.shape)):
            if i == j:
                l_num *= 1
                l_denum *= 1
            else:
                l_num *= (x - X[i])
                l_denum *= (X[j] - X[i])
        L += Y[j] * l_num / l_denum
    return collect(expand(L), x)


def nodes(f, p, n, a=-15, b=15):
    if p == 0:
        X = np.arange(a, b + 1, (b - a) / n)
        Y = np.array(f(X))
        return X, Y
    else:
        X = np.array([(((b - a) * np.cos((2 * i + 1) * np.pi / (2 * n + 2)) + (b + a)) / 2) for i in range(n + 1)])
        Y = np.array(f(X))
        return X, Y


arr = np.arange(-15, 16, 0.01)
fig1, ax1 = plt.subplots()
ax1.set_ylim([-30, 30])

fig2, ax2 = plt.subplots()
ax2.set_ylim([-30, 30])

x = symbols('x')
line = ax1.plot(arr, f(arr), label='f(x)')

for i in [10, 7, 5]:
    Lf1 = lagrange(nodes(f, 0, i)[0], nodes(f, 0, i)[1])
    print("Для функции f с", i, "рандомными узлами: ", '\n', Lf1)

    Lf2 = lagrange(nodes(f, 1, i)[0], nodes(f, 1, i)[1])
    print("Для функции f с", i, "узлами, минимизирующими методическую погрешность: ", '\n', Lf2)
    r=i+1
    ax1.plot(arr, [Lf1.subs(x, arr[j]) for j in range(np.prod(arr.shape))], label='random with %d nodes' %r)
    ax1.plot(arr, [Lf2.subs(x, arr[j]) for j in range(np.prod(arr.shape))], label='minerr with %d nodes' %r)


Lh1 = lagrange(nodes(h, 0, 5)[0], nodes(h, 0, 5)[1])
print("Для функции h с 5 рандомными узлами: ", '\n', Lh1)

Lh2 = lagrange(nodes(h, 1, 5)[0], nodes(h, 1, 5)[1])
print("Для функции h с 5 узлами, минимизирующими методическую погрешность: ", '\n', Lh2)


ax2.plot(arr, f(arr), label='f(x)')
ax2.plot(arr, [Lf1.subs(x, arr[j]) for j in range(np.prod(arr.shape))], label='random for f with 6 nodes')
ax2.plot(arr, [Lf2.subs(x, arr[j]) for j in range(np.prod(arr.shape))], label='minerr for f with 6 nodes')
ax2.plot(arr, [Lh1.subs(x, arr[j]) for j in range(np.prod(arr.shape))], label='random for h with 6 nodes')
ax2.plot(arr, [Lh2.subs(x, arr[j]) for j in range(np.prod(arr.shape))], label='minerr for h with 6 nodes')

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')
plt.show()




