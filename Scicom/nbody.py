import numpy as np
from functools import partial
from astropy import constants as const
from rk4 import rk4_integration
import matplotlib.pyplot as plt


# from scicom.coords import distance_vec, distance_sca


def nbody(positions, velocity, mass, labels, dt, time):
    positions = np.array(positions.value)
    velocity = np.array(velocity.value)
    mass = np.array(mass.value)
    ode = partial(_diff_eq, m=mass)
    vals = np.concatenate((positions, velocity), axis=-1)

    return rk4_integration(ode=ode, start_vals=vals, dt=dt, stop_time=time)


"""def _diff_eq(vals, m): 
    #acceleration derived form Newton`s law of gravitation => a(vector) = Gm/r^3 *r(vector) 
    out = np.zeros(vals.shape) 
    out[..., :3] = vals[..., 3:] 

    dist = distance_vec(vals[..., :3]) 

    with np.errstate(divide="ignore", invalid="ignore"): 
        acc = (const.G.value * m[None, :, None] * dist / (distance_sca(vals[..., :3]) ** 3)[:, :, None]) 
    acc[~np.isfinite(acc)] = 0 
    out[..., 3:] = np.sum(acc, axis=1) 
    return out"""


def _diff_eq(vals, m):
    pos = vals[..., :3]
    vel = vals[..., 3:]

    out = np.zeros(vals.shape)
    out[:, :3] = vel

    acc = np.zeros(pos.shape)
    for a in range(len(m)):
        for b in range(len(m)):
            if a == b:
                continue
            acc[a] += const.G.value * m[b] * (pos[b] - pos[a]) / np.linalg.norm(pos[b] - pos[a]) ** 3
    out[:, 3:] = acc
    return out
