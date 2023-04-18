import numpy as np
import nbody
import solar_bodies
from astropy import units
import matplotlib.pyplot as plt

preset = solar_bodies.bodies_masses()
solar_bodies_pos = preset[0]
solar_bodies_vel = preset[1]
solar_bodies_mas = preset[2]


n = 0
asteroid_pos = np.random.random((n, 3)) * units.meter   # mit irgend einem Abstand multiplizieren (z.B. Asteroidengürtel)
asteroid_vel = np.random.random((n, 3)) * units.meter/units.second
asteroid_mas = np.random.random(n) * units.kg

all_pos = np.concatenate((solar_bodies_pos, asteroid_pos), axis=0)
all_vel = np.concatenate((solar_bodies_vel, asteroid_vel), axis=0)
all_mas = np.concatenate((solar_bodies_mas, asteroid_mas))

dt = 1800/4
t_t = 31536000/4


sim = nbody.nbody(all_pos, all_vel, all_mas, None, dt, t_t)     # 6-dim array aus pos und vel


val_0 = []
for i in range(int(t_t/dt)):
    val_0.append(np.linalg.norm(sim[i][0, :][:3]))
#print(val_0)

val_1 = []
for i in range(int(t_t/dt)):
    val_1.append(np.linalg.norm(sim[i][1, :][:3]))
#print(val_1)

val_2 = []
for i in range(int(t_t/dt)):
    val_2.append(np.linalg.norm(sim[i][2, :][:3]))
#print(val_2)

val_3 = []
for i in range(int(t_t/dt)):
    val_3.append(np.linalg.norm(sim[i][3, :][:3]))
#print(val_3)

val_4 = []
for i in range(int(t_t/dt)):
    val_4.append(np.linalg.norm(sim[i][4, :][:3]))
#print(val_4)

val_5 = []
for i in range(int(t_t/dt)):
    val_5.append(np.linalg.norm(sim[i][5, :][:3]))
#print(val_5)


val_6 = []
for i in range(int(t_t/dt)):
    val_6.append(np.linalg.norm(sim[i][6, :][:3]))
#print(val_6)

val_7 = []
for i in range(int(t_t/dt)):
    val_7.append(np.linalg.norm(sim[i][7, :][:3]))
#print(val_7)

val_8 = []
for i in range(int(t_t/dt)):
    val_8.append(np.linalg.norm(sim[i][8, :][:3]))
#print(val_8)

val_9 = []
for i in range(int(t_t/dt)):
    val_9.append(np.linalg.norm(sim[i][9, :][:3]))
#print(val_9)


plt.plot(range(int(t_t/dt)), val_0, label="sun")
plt.plot(range(int(t_t/dt)), val_1, label="mercury")
plt.plot(range(int(t_t/dt)), val_2, label="venus")
plt.plot(range(int(t_t/dt)), val_3, label="earth")
plt.plot(range(int(t_t/dt)), val_4, label="moon")
plt.plot(range(int(t_t/dt)), val_5, label="mars")
plt.plot(range(int(t_t/dt)), val_6, label="jupiter")
plt.plot(range(int(t_t/dt)), val_7, label="saturn")
plt.plot(range(int(t_t/dt)), val_8, label="uranus")
plt.plot(range(int(t_t/dt)), val_9, label="neptune")

plt.legend(loc="upper right")
plt.show()