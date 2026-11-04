import heapq
import matplotlib.pyplot as plt
import numpy as np

# Heuristic for A* (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 1. Dijkstra's Algorithm (Blind search: explores equally in all directions)
def run_dijkstra(grid_size, obstacles, start, goal):
    pq = [(0, start)]
    costs = {start: 0}
    parents = {}
    explored = []

    while pq:
        cost, current = heapq.heappop(pq)
        explored.append(current)

        if current == goal:
            break

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (r + dr, c + dc)
            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                if neighbor not in obstacles:
                    new_cost = cost + 1
                    if neighbor not in costs or new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        parents[neighbor] = current
                        heapq.heappush(pq, (new_cost, neighbor))

    # Reconstruct path
    path = []
    step = goal
    while step in parents:
        path.append(step)
        step = parents[step]
    path.append(start)
    path.reverse()
    return path, explored

# 2. A* Search Algorithm (Guided search: uses the heuristic compass)
def run_astar(grid_size, obstacles, start, goal):
    pq = [(0, 0, start)]
    costs = {start: 0}
    parents = {}
    explored = []

    while pq:
        _, cost, current = heapq.heappop(pq)
        explored.append(current)

        if current == goal:
            break

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (r + dr, c + dc)
            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                if neighbor not in obstacles:
                    new_cost = cost + 1
                    if neighbor not in costs or new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        priority = new_cost + heuristic(neighbor, goal)
                        parents[neighbor] = current
                        heapq.heappush(pq, (priority, new_cost, neighbor))

    # Reconstruct path
    path = []
    step = goal
    while step in parents:
        path.append(step)
        step = parents[step]
    path.append(start)
    path.reverse()
    return path, explored


# --- RUN & VISUALIZE SIDE-BY-SIDE ---
if __name__ == "__main__":
    grid_size = 25
    start = (0, 0)
    goal = (24, 24)

    # Obstacles
    obstacles = set()
    for r in range(5, 20):
        obstacles.add((r, 12))
    for c in range(6, 18):
        obstacles.add((18, c))

    d_path, d_explored = run_dijkstra(grid_size, obstacles, start, goal)
    a_path, a_explored = run_astar(grid_size, obstacles, start, goal)

    print("=" * 45)
    print("      ALGORITHM BENCHMARK RESULTS")
    print("=" * 45)
    print(f"Dijkstra Visited Tiles : {len(d_explored)}")
    print(f"A* Visited Tiles       : {len(a_explored)}")
    saved_effort = ((len(d_explored) - len(a_explored)) / len(d_explored)) * 100
    print(f"Effort Saved by A*     : {saved_effort:.1f}%")
    print("=" * 45)

    # Side-by-side plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    runs = [
        ("Dijkstra (No Heuristic / Blind)", d_explored, d_path, axes[0]),
        ("A* (Guided by Manhattan Distance)", a_explored, a_path, axes[1])
    ]

    for title, explored, path, ax in runs:
        grid_data = np.zeros((grid_size, grid_size))
        for r, c in obstacles:
            grid_data[r, c] = 1

        ax.imshow(grid_data, cmap="Greys", origin="upper")
        
        ex_r, ex_c = zip(*explored)
        ax.scatter(ex_c, ex_r, color="lightskyblue", s=20, label="Explored Nodes")
        
        pr, pc = zip(*path)
        ax.plot(pc, pr, color="limegreen", linewidth=3, label="Optimal Path")
        
        ax.scatter([start[1]], [start[0]], color="blue", s=100, label="Start")
        ax.scatter([goal[1]], [goal[0]], color="red", marker="*", s=160, label="Goal")
        
        ax.set_title(f"{title}\nNodes Explored: {len(explored)}", fontsize=11)
        ax.legend(loc="upper left")
        ax.grid(True, linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.show()