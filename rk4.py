import numpy as np


def rk4_step(ode: callable, vals: np.array, dt: float):
    """
    time-independent RK4 - integration.
    :param ode: callable, the system of ODEs to be solved
    :param vals: np.array-like, old system state
    :param dt: float, time step for integration
    :return: np.array or array-like, new system state
    """
    k1 = dt * ode(vals)
    k2 = dt * ode(vals + k1/2)
    k3 = dt * ode(vals + k2/2)
    k4 = dt * ode(vals + k3)

    vals += (k1 + 2*k2 + 2*k3 + k4)

    return vals


def rk4_integration(ode, start_vals, dt, stop_time):
    out = []

    for i in range(int(stop_time/dt)):
        out.append(rk4_step(ode, start_vals, dt).copy())
        #yield rk4_step(ode, start_vals, dt)

    return out