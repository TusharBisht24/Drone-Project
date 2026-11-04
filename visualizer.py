import matplotlib.pyplot as plt
import numpy as np
from pathfinding import find_drone_route

# 1. Set up a 20x20 city grid
grid_size = 20
hospital_base = (0, 0)        # Top-left corner
casualty_target = (19, 19)    # Bottom-right corner

# 2. Add some tall buildings / no-fly obstacles right in the center path
obstacles = set()
# Vertical wall
for r in range(4, 16):
    obstacles.add((r, 10))
# Horizontal barricade
for c in range(5, 12):
    obstacles.add((15, c))

# 3. Calculate the route using our A* algorithm
flight_path, explored = find_drone_route(grid_size, obstacles, hospital_base, casualty_target)

print(f"Total tiles explored by A*: {len(explored)}")
print(f"Final Path Length: {len(flight_path)} steps")

# 4. Draw the map
grid_display = np.zeros((grid_size, grid_size))
for r, c in obstacles:
    grid_display[r, c] = 1  # 1 means obstacle

plt.figure(figsize=(8, 8))
plt.imshow(grid_display, cmap="Greys", origin="upper")

# Draw where the drone searched (Blue dots)
ex_r, ex_c = zip(*explored)
plt.scatter(ex_c, ex_r, color="skyblue", s=25, label="Explored Nodes (A* Search)")

# Draw the final chosen flight line (Green line)
path_r, path_c = zip(*flight_path)
plt.plot(path_c, path_r, color="limegreen", linewidth=3, label="Optimal Drone Flight Route")

# Draw the Start and End points
plt.scatter([hospital_base[1]], [hospital_base[0]], color="blue", s=140, zorder=5, label="Hospital Hub")
plt.scatter([casualty_target[1]], [casualty_target[0]], color="crimson", marker="*", s=220, zorder=5, label="Emergency Drop Target")

plt.title("A* Emergency Drone Navigation with Obstacle Avoidance", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True, color="lightgray", linestyle="--", linewidth=0.5)

# Pop up the visual window!
plt.show()