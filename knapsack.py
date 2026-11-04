def solve_drone_packing(weights, values, items, max_capacity):
    n = len(weights)
    
    # Create a 2D table filled with zeros
    dp = [[0] * (max_capacity + 1) for _ in range(n + 1)]

    # Fill the table step-by-step
    for i in range(1, n + 1):
        for w in range(1, max_capacity + 1):
            current_weight = weights[i - 1]
            current_val = values[i - 1]

            if current_weight <= w:
                # Decide: Take it OR Leave it?
                value_if_taken = current_val + dp[i - 1][w - current_weight]
                value_if_left = dp[i - 1][w]
                dp[i][w] = max(value_if_taken, value_if_left)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to see which items were picked
    w = max_capacity
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(items[i - 1])
            w -= weights[i - 1]

    return dp[n][max_capacity], chosen_items


if __name__ == "__main__":
    # Test data: list of emergency items
    names = ["Medicine Kit", "Defibrillator", "Water Rations", "Food Packs"]
    weights = [5, 10, 15, 12]     # in kg
    values = [50, 120, 160, 140]  # emergency priority score
    drone_limit = 20              # max weight drone can carry in kg

    best_score, packed = solve_drone_packing(weights, values, names, drone_limit)
    
    print("-" * 40)
    print("🚁 DRONE PAYLOAD OPTIMIZATION (KNAPSACK)")
    print("-" * 40)
    print(f"Drone Weight Limit : {drone_limit} kg")
    print(f"Total Priority Score: {best_score}")
    print(f"Items Packed In Drone: {packed}")
    print("-" * 40)