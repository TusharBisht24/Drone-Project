import heapq

# This is our heuristic "compass":
# It guesses the distance to the goal using straight grid steps (Manhattan distance)
def get_distance_estimate(current_cell, goal_cell):
    return abs(current_cell[0] - goal_cell[0]) + abs(current_cell[1] - goal_cell[1])


def find_drone_route(grid_size, obstacles, start_pos, target_pos):
    # Priority Queue stores: (estimated_total_score, cost_walked_so_far, cell_position)
    # The heap always pops the most promising tile first!
    open_queue = []
    heapq.heappush(open_queue, (0, 0, start_pos))

    # Keep track of where we came from so we can draw the final path
    parent_map = {}
    
    # Keep track of exact distance traveled from the start to each cell
    cost_to_reach = {start_pos: 0}
    
    # Store visited cells to visualize later
    explored_cells = []

    while open_queue:
        _, current_cost, current_cell = heapq.heappop(open_queue)
        explored_cells.append(current_cell)

        # Did we reach the casualty zone?
        if current_cell == target_pos:
            break

        # Check adjacent tiles: Up, Down, Left, Right
        row, col = current_cell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            neighbor = (row + dr, col + dc)

            # 1. Make sure it's inside the city boundary
            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                # 2. Make sure it's not a skyscraper/obstacle
                if neighbor not in obstacles:
                    step_cost = current_cost + 1

                    # If this is a new cell or we found a shorter way to reach it
                    if neighbor not in cost_to_reach or step_cost < cost_to_reach[neighbor]:
                        cost_to_reach[neighbor] = step_cost
                        
                        # Priority = Cost so far (g) + Guess to target (h)
                        priority_score = step_cost + get_distance_estimate(neighbor, target_pos)
                        heapq.heappush(open_queue, (priority_score, step_cost, neighbor))
                        
                        parent_map[neighbor] = current_cell

    # Backtrack from target back to start to form the line
    flight_path = []
    step = target_pos
    while step in parent_map:
        flight_path.append(step)
        step = parent_map[step]
    
    flight_path.append(start_pos)
    flight_path.reverse()  # Flip it so it goes Start -> Target

    return flight_path, explored_cells