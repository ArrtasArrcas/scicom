import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the simulation parameters
num_bodies = 3  # Number of bodies
G = 1  # Gravitational constant
dt = 0.01  # Time step
num_steps = 1000  # Number of simulation steps

# Set up the initial conditions for a collinear configuration
masses = np.array([1, 1, 1])  # Masses of the bodies
positions = np.array([[-0.97000436, 0.24308753], [0.97000436, -0.24308753], [0, 0]])  # Initial positions
velocities = np.array([[0.4662036850, 0.4323657300], [0.4662036850, 0.4323657300], [-0.93240737, -0.86473146]])  # Initial velocities

# Create a figure and axis for the animation
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 5))
points, = ax.plot([], [], 'bo', ms=6)

# Function to compute the gravitational forces
def compute_forces(positions):
    forces = np.zeros_like(positions)
    for i in range(num_bodies):
        for j in range(num_bodies):
            if i != j:
                delta_r = positions[j] - positions[i]
                force = G * masses[i] * masses[j] * delta_r / np.linalg.norm(delta_r)**3
                forces[i] += force
    return forces

# Function to update the animation frame
def update(frame):
    global positions, velocities

    # Compute the forces at the current positions
    k1v = compute_forces(positions)
    k1x = velocities

    # Compute the intermediate positions and velocities
    k2x = velocities + 0.5 * dt * k1v
    k2v = compute_forces(positions + 0.5 * dt * k1x)

    k3x = velocities + 0.5 * dt * k2v
    k3v = compute_forces(positions + 0.5 * dt * k2x)

    k4x = velocities + dt * k3v
    k4v = compute_forces(positions + dt * k3x)

    # Update the positions and velocities using RK4 integration
    positions += dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
    velocities += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)

    # Update the animation frame
    points.set_data(positions[:, 0], positions[:, 1])

    return points,

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Create the animation
anim = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True, interval=0.1)

# Save the animation as a .mp4 file
#anim.save('n_body_animation.mp4', writer='ffmpeg')
plt.xlim([-1.5, 1.5])
plt.ylim([-0.75, 0.75])
# Display the animation
plt.show()
