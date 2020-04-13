import numpy as np


def gauss(A, b):
    d1, d2 = A.shape, b.shape
    a = np.concatenate((A, b), axis = 1)
    x = np.zeros(d2[0])
    n = d1[0]
    for i in range(n):
        x[i] = a[i][n]
        
    for k in range(1, n):
        for j in range(k, n):
            m = a[j][k-1] / a[k-1][k-1]
            for i in range(0, n + 1):
                a[j][i] = a[j][i] - m * a[k-1][i]
            x[j] = x[j] - m * x[k-1]
            
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x


def iterative(A, b, eps):
    d1, d2 = A.shape, b.shape
    B, c = np.zeros(shape = (d1[0], d1[1])), np.zeros(d2[0])
    
    for j in range(0, d1[0]):
        for i in range(0, d1[1]):
            if (i == j):
                B[i][i] = 0
            else:
                B[i][j] = -(A[i][j] / A[i][i])
    
    for i in range(0, d2[0]):
        c[i] = b[i] / A[i][i]

    approx = c
    k = 0
    while True:
        k += 1
        prev = approx
        approx = np.add(c, np.dot(B, approx))
        if (np.linalg.norm(np.subtract(approx, prev)) < eps / (np.linalg.norm(A))):
            print("Iterations: ", k)
            return approx

        
def bad_cond(size, eps, n):
    assert size > 0
    val = eps * n
    A = np.full((size, size), val)
    for i in range(size):
        A[i, i] += round(1, 6)
        for j in range(i + 1, size):
            A[i, j] = -1 - val
    b = np.full((size, 1), -1)
    b[-1][0] = 1
    return A, b


def output(A, b, eps):
    print("A: ")
    print(A)
    print("b: ")
    print(b)
    print("Gauss Method: ", ["%.10f" % i for i in gauss(A, b)])
    print("Itetative Method: ", ["%.10f" % i for i in iterative(A, b, eps)])

n, eps = 10, 1e-6
A = np.array([
             [n + 2, 1, 1],
             [1, n + 4, 1],
             [1, 1, n + 6]
        ], 'float')
b = np.array([[n + 4], [n + 6], [n + 8]], 'float')
output(A, b, eps)

for i in range(2, 5):
    print("_" * 80)
    A_bad, b_bad = bad_cond(i, 10**(-1 - i), n)
    output(A_bad, b_bad, eps)