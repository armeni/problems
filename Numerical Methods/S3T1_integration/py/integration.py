import numpy as np
import math


def mu(z1, z0, a, alpha, s):
    mu0 = ((z1 - a) ** (1 - alpha) - (z0 - a) ** (1 - alpha)) / (1 - alpha)
    mu = [mu0]
    for i in range(1, s + 1):
        c = np.poly([-a] * i)[::-1]
        mu_i = sum([c[j] * ((z1 - a) ** (j + 1 - alpha) - (z0 - a) ** (j + 1 - alpha)) / (j + 1 - alpha) for j in range(0, i + 1)])
        mu.append(mu_i)
    return mu


def nu(z1, z0, b, beta, s):
    nu0 = ((b - z0) ** (1 - beta) - (b - z1) ** (1 - beta)) / (1 - beta)
    nu = [nu0]
    for i in range(1, s + 1):
        c = (-1) ** i * np.poly([b] * i )[::-1]
        nu_i = - sum([c[j] * ((b - z1) ** (j + 1 - beta) - (b - z0) ** (j + 1 - beta)) / (j + 1 - beta) for j in range(0, i + 1)])
        nu.append(nu_i)
    return nu


def moments(max_s, xl, xr, a=None, b=None, alpha=0.0, beta=0.0):
    """
    compute 0..max_s moments of the weight p(x) = 1 / (x-a)^alpha / (b-x)^beta over [xl, xr]
    """

    assert alpha * beta == 0, f'alpha ({alpha}) and/or beta ({beta}) must be 0'
    if alpha != 0.0:
        assert a is not None, f'"a" not specified while alpha != 0'
        return mu(xr, xl, a, alpha, max_s)
    if beta != 0.0:
        assert b is not None, f'"b" not specified while beta != 0'
        return nu(xr, xl, b, beta, max_s)

    if alpha == 0 and beta == 0:
        return [(xr ** s - xl ** s) / s for s in range(1, max_s + 2)]

    raise NotImplementedError


def runge(s0, s1, m, L):
    """
    estimate m-degree errors for s0 and s1
    """
    d0 = np.abs(s1 - s0) / (1 - L ** -m)
    d1 = np.abs(s1 - s0) / (L ** m - 1)
    return d0, d1


def aitken(s0, s1, s2, L):
    """
    estimate accuracy degree
    s0, s1, s2: consecutive composite quads
    return: accuracy degree estimation
    """
    return - (np.log(np.abs((s2 - s1)/(s1 - s0)))/np.log(L))


def quad(func, x0, x1, xs, **kwargs):
    """
    func: function to integrate
    x0, x1: interval to integrate on
    xs: nodes
    **kwargs passed to moments()
    """
    m = moments(len(xs) - 1, x0, x1, **kwargs)
    x = np.vander(xs)[:, ::-1].T
    res = np.sum(np.linalg.solve(x, m).dot(func(xs)))
    return res


def quad_gauss(func, x0, x1, n, **kwargs):
    """
    func: function to integrate
    x0, x1: interval to integrate on
    n: number of nodes
    """
    m = moments(2 * n - 1, x0, x1, **kwargs)
    mu_j = [[m[j + s] for j in range(n)] for s in range(n)]
    mu_s = [-m[n + s] for s in range(n)]
    a = np.linalg.solve(mu_j, mu_s)
    x = np.roots(np.append(a, 1)[::-1])
    xs = [[i ** s for i in x] for s in range(n)]
    res = np.sum(np.linalg.solve(xs, m[:n]).dot(func(x)))
    return res


def composite_quad(func, x0, x1, n_intervals, n_nodes, **kwargs):
    """
    func: function to integrate
    x0, x1: interval to integrate on
    n_intervals: number of intervals
    n_nodes: number of nodes on each interval
    """
    interval = np.linspace(x0, x1, n_intervals + 1)
    res = sum([quad(func, interval[i], interval[i + 1], np.linspace(interval[i], interval[i + 1], n_nodes), **kwargs) for i in range(n_intervals)])
    return res


def integrate(func, x0, x1, tol):
    """
    integrate with error <= tol
    return: result, error estimation
    """
    nodes = 3
    L = 2
    h0 = x1 - x0
    error = tol + 1
    while error > tol:
        h = [h0 / L ** i for i in range(3)]
        n = [int((x1 - x0) / i) for i in h]
        quad = [composite_quad(func, x0, x1, n_interval, nodes) for n_interval in n]
        m = aitken(*quad, L)
        error = runge(*quad[1:], m, L)[0]
        h0 = quad[2] * (tol / error) ** (1 / m)
    return quad[2], error
