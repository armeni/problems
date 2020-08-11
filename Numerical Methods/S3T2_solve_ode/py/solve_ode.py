import enum
import numpy as np

from S3T2_solve_ode.py.one_step_methods import OneStepMethod
from S3T2_solve_ode.py.one_step_methods import ExplicitEulerMethod


class AdaptType(enum.Enum):
    RUNGE = 0
    EMBEDDED = 1


def fix_step_integration(method: OneStepMethod, func, y_start, ts):
    """
    performs fix-step integration using one-step method
    ts: array of timestamps
    return: list of t's, list of y's
    """
    ys = [y_start]

    for i, t in enumerate(ts[:-1]):
        y = ys[-1]

        y1 = method.step(func, t, y, ts[i + 1] - t)
        ys.append(y1)

    return ts, ys


def adaptive_step_integration(method: OneStepMethod, func, y_start, t_span,
                              adapt_type: AdaptType,
                              atol, rtol):
    """
    performs adaptive-step integration using one-step method
    t_span: (t0, t1)
    adapt_type: Runge or Embedded
    tolerances control the error:
        err <= atol
        err <= |y| * rtol
    return: list of t's, list of y's
    """
    y = y_start
    t, t_end = t_span

    ts = [t]
    ys = [y]
    p = method.p

    delta = (1 / max(np.abs(t), np.abs(t_end))) ** (p + 1) + np.linalg.norm(func(t, y)) ** (p + 1)
    h1 = (atol / delta) ** (1 / (p + 1))
    yh = y + h1 * func(t, y)
    delta = (1 / max(np.abs(t), np.abs(t_end))) ** (p + 1) + np.linalg.norm(func(t + h1, yh)) ** (p + 1)
    h2 = (atol / delta) ** (1 / (p + 1))
    h = min(h1, h2)

    while t < t_end:
        t = ts[-1]
        y = ys[-1]
        h = min(t_end - t, h)

        if adapt_type == AdaptType.RUNGE:
            y1 = method.step(func, t, y, h)
            y2 = method.step(func, t + h / 2, method.step(func, t, y, h / 2), h / 2)
            error = (y2 - y1) / (1 - 2 ** (-p))
        else:
            y1, error = method.embedded_step(func, t, y, h)

        error = np.linalg.norm(error)
        tol = min(rtol * np.linalg.norm(y1), atol)

        if error > tol:
            h *= 0.5

        elif error < tol * 1 / 2 ** (p + 1):
            ts.append(t + h)
            ys.append(y1)
            h *= 2

        else:
            ts.append(t + h)
            ys.append(y1)

    return ts, ys

