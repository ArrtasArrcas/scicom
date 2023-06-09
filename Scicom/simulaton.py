import anime_plot
import spaß_mit_asteroiden

"""bodies = ["earth", "sun", "moon"] 
preset = test_bodies.solar_system 

v, x, m, names = preset 

step = 36000 
dt = 1000 

newt = nbody.nbody(*preset, step, n*step) 
ref = test_bodies.get_series(bodies=bodies, dt=step, duration=n*step) 
"""

"""def asteroids(n, dt, t_t): 
    mass = np.random.random(n)*1000000 + 50000 
    p = np.random.random((n, 3))*10000 
    v = np.random.random((n, 3))*0 

    return nbody.nbody(p, v, mass, dt, t_t)"""

# plot.plot(asteroids(10, 10000, 10000000))

"""step = 36000 
n = 1000 

preset = solar_bodies.bodies_masses() #nur Zeugs aus Sonnens 
pos = preset[0] 
print(preset) 
newt = nbody.nbody(*preset, step, n*step)"""

anime_plot.plotting(spaß_mit_asteroiden.sim)