from datetime import datetime, timedelta
from astropy import coordinates, time, units
from typing import Union

import numpy as np

solar_system = ["sun", "mercury", "venus", "earth", "moon", "mars", "jupiter", "saturn", "uranus", "neptune"]


def bodies_masses(*, bodies=None, t=datetime.fromisocalendar(2000, 1, 1)):
    timestamp = time.Time(t, format="datetime")

    if bodies is None:
        bodies = solar_system
    elif not set(solar_system).issuperset(bodies):
        raise ValueError("ka")

    masses = {"sun": 1.9885E30,
              "mercury": 3.30E23,
              "venus": 4.87E24,
              "earth": 5.97E24,
              "moon": 7.3E22,
              "mars": 6.42E23,
              "jupiter": 1.898E27,
              "saturn": 5.68E26,
              "uranus": 8.68E25,
              "neptune": 1.02E26}

    pos = []
    vel = []
    mas = np.array([masses[body] for body in bodies]) * units.kg

    for body in bodies:
        p, v = coordinates.get_body_barycentric_posvel(body, time=timestamp)
        pos.append(p.xyz.to(units.meter))
        vel.append(v.xyz.to(units.meter / units.second))

    return np.array(pos) * units.meter, np.array(vel) * units.meter / units.second, mas, bodies


def get_series(*,
               bodies: list = None,
               start: datetime = datetime.fromisocalendar(2000, 1, 1),
               stop: datetime = None,
               duration: Union[float, int, timedelta] = None,
               dt: Union[float, int, timedelta]):

    if bodies is None:
        bodies = solar_system
    if dt is None:
        dt = timedelta(days=1)
    elif type(dt) is not timedelta:
        dt = timedelta(seconds=dt)
    if stop is None and duration is None:
        stop = start + timedelta(days=10)
    elif stop is None:
        if type(duration) is not timedelta:
            duration = timedelta(seconds=duration)
        stop = start + duration


    def gen(bod, stt, stp, tm):
        curr =stt
        while curr < stp:
            curr += tm
            timestep = time.Time(curr, format="datetime")
            pos = np.array([
                (lambda x, v: np.concatenate((x.xyz.to(units.m).value, v.xyz.to(units.m/units.s).value)))
                (*coordinates.get_body_barycentric_posvel(body, time=timestep)) for body in bod])
            yield pos

    _, _, mas, _ = bodies_masses(bodies=bodies, t=start)
    times =[]
    now = start
    now_s = 0
    while now < stop:
        times.append(now_s)
        now += dt
        now_s += dt.total_seconds()

    return gen(bodies, start, stop, dt), np.array(times), np.array(mas.value), bodies

#nur für sonnensystem