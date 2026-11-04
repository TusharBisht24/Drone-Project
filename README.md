# 🚁 Emergency Drone Delivery Optimization (DAA)

An autonomous drone routing framework in Python that applies core **Design and Analysis of Algorithms (DAA)** concepts to solve three real-world disaster relief challenges:

* **Payload Packing (0/1 Knapsack):** Uses Dynamic Programming to select the highest-priority medical supplies and rations within strict weight limits[cite: 1].
* **Obstacle Navigation (A* Search):** Guides the drone around urban buildings using a Manhattan distance heuristic, cutting search exploration by up to 70% compared to Dijkstra[cite: 1, 2].
* **Multi-Stop Routing (Held-Karp TSP):** Uses Dynamic Programming with bitmasking to compute the shortest closed flight path across multiple relief camps in $O(n^2 2^n)$ time[cite: 1].

---

### ⚡ Highlights
* **Language:** Python 3
* **Paradigms:** Dynamic Programming, Heuristic Graph Search, Bitmask DP[cite: 1]
* **Visualization:** Side-by-side search visualizer and empirical runtime scalability plots[cite: 2]

---

### 🚀 Quick Start
```bash
python algorithms/knapsack.py      # Optimal cargo selection
python visualizer/compare.py       # Visual pathfinding benchmark
python algorithms/tsp.py           # Multi-stop relief tour
python visualizer/complexity_graph.py  # Runtime scaling curve
