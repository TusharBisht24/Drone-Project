import math

def held_karp_tsp(dist_matrix):
    """
    Solves TSP using Dynamic Programming + Bitmasking.
    Time Complexity: O(n^2 * 2^n)
    """
    n = len(dist_matrix)
    memo = {}

    # mask: binary integer representing visited cities (e.g. 0b0101 means city 0 and 2 visited)
    # u: current city index
    def visit(mask, u):
        # Base case: All cities visited, return distance back to base (city 0)
        if mask == (1 << n) - 1:
            return dist_matrix[u][0], [0]

        state = (mask, u)
        if state in memo:
            return memo[state]

        min_cost = float('inf')
        best_path = []

        # Try visiting every unvisited neighbor
        for v in range(n):
            if not (mask & (1 << v)):
                cost, path = visit(mask | (1 << v), v)
                total = dist_matrix[u][v] + cost
                if total < min_cost:
                    min_cost = total
                    best_path = [v] + path

        memo[state] = (min_cost, best_path)
        return memo[state]

    # Start from base station (city 0)
    total_cost, full_path = visit(1, 0)
    return total_cost, [0] + full_path


if __name__ == "__main__":
    locations = [
        "Base Hospital",
        "Shelter Alpha",
        "Field Hospital Beta",
        "Refugee Camp Gamma",
        "Evacuation Point Delta"
    ]

    # Distance matrix between drop points (in km)
    distances = [
        [0, 12, 29, 22, 13],
        [12, 0, 19, 11, 25],
        [29, 19, 0, 17, 10],
        [22, 11, 17, 0, 15],
        [13, 25, 10, 15, 0]
    ]

    cost, path = held_karp_tsp(distances)

    print("=" * 55)
    print("🚁 MULTI-STOP EMERGENCY ROUTE OPTIMIZATION (TSP)")
    print("=" * 55)
    print(f"Optimal Minimum Distance: {cost} km")
    print("Flight Sequence:")
    for idx, stop in enumerate(path):
        arrow = " -> " if idx < len(path) - 1 else ""
        print(f"{locations[stop]}{arrow}", end="")
    print("\n" + "=" * 55)