import numpy as np

N = 18
eps = 1e-6

A = np.array([[4, 1, 1],
              [1, 2 * (3 + 0.1 * N), -1],
              [1, -1, 2 * (4 + 0.1 * N)]])

b = np.array([[1.],
              [-2.],
              [3.]])

x0 = np.array([[0.],
                [0.],
                [0.]])


def f(x):
    return (np.dot(np.dot(x.transpose(), A), x))[0][0] / 2 + np.dot(x.transpose(), b)[0][0] + N


def mngs(A, b, eps):
    k = 0
    x = b
    q = np.dot(A, x) + b
    while np.linalg.norm(q) > eps:
        k += 1
        m = -np.dot(q.T, q) / np.dot(np.dot(q.T, A), q)
        x = x + m * q
        q = np.dot(A, x) + b
    return x, k


def mnps(A, b, eps):
    k = 0
    x = b.copy()
    n = A.shape[0]
    q = np.dot(A, x) + b
    while np.linalg.norm(q) > eps:
        i = k % n
        k += 1
        m = -q[i][0] / A[i][i]
        x[i][0] = x[i][0] + m
        q = np.dot(A, x) + b
    return x, k


def gauss(A, b):
    d1, d2 = A.shape, b.shape
    a = np.concatenate((A, b), axis=1)
    x = np.zeros(d2[0])
    n = d1[0]
    for i in range(n):
        x[i] = a[i][n]

    for k in range(1, n):
        for j in range(k, n):
            m = a[j][k - 1] / a[k - 1][k - 1]
            for i in range(0, n + 1):
                a[j][i] = a[j][i] - m * a[k - 1][i]
            x[j] = x[j] - m * x[k - 1]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x


print('Метод наискорейшего градиентного спуска')
x_ming, k = mngs(A, b, eps)
print('Минимум функции: ', f(x_ming))
print('Достигается в точке: ', x_ming.T)
print('Кол-во итераций: ', k)
print('\n')

print('Метод наискорейшего покоординатного спуска')
x_minp, k = mnps(A, b, eps)
print('Минимум функции: ', f(x_minp))
print('Достигается в точке: ', x_minp.T)
print('Кол-во итераций: ', k)
print('\n')

print('Точный метод Гаусса (для сравнения): ', gauss(A, -b))
