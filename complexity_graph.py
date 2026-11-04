import time
import matplotlib.pyplot as plt
from compare import run_dijkstra, run_astar

sizes = [10, 15, 20, 25, 30]
dijkstra_times = []
astar_times = []

for size in sizes:
    start = (0, 0)
    goal = (size - 1, size - 1)
    obstacles = set()
    # Add a sparse line of obstacles
    for r in range(size // 4, 3 * size // 4):
        obstacles.add((r, size // 2))

    # Benchmark Dijkstra
    t0 = time.perf_counter()
    run_dijkstra(size, obstacles, start, goal)
    dijkstra_times.append((time.perf_counter() - t0) * 1000)

    # Benchmark A*
    t0 = time.perf_counter()
    run_astar(size, obstacles, start, goal)
    astar_times.append((time.perf_counter() - t0) * 1000)

plt.figure(figsize=(8, 5))
plt.plot(sizes, dijkstra_times, marker='o', label="Dijkstra's (Explores radial frontier)")
plt.plot(sizes, astar_times, marker='s', label="A* Search (Guided by Heuristic)")
plt.title("DAA Performance Benchmark: Execution Time vs Grid Scale (N x N)", fontsize=11)
plt.xlabel("Grid Dimension N")
plt.ylabel("Time Taken (milliseconds)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()