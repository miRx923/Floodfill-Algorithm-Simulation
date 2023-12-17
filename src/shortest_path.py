""" File for finding the shortest path in 2D field """

import field_utils as fu

def find_shortest_path(field, start_x, start_y, end_x, end_y):
    """Function for finding and visualising the shortest path"""

    # Error checking
    if not all(isinstance(i, int) for i in [start_x, start_y, end_x, end_y]):
        raise TypeError("All start_x, start_y, end_x, and end_y must be integers.")

    if start_x < 0 or start_x >= len(field) or start_y < 0 or start_y >= len(field[0]):
        raise ValueError("start_x and start_y must be within the field dimensions.")

    if end_x < 0 or end_x >= len(field) or end_y < 0 or end_y >= len(field[0]):
        raise ValueError("end_x and end_y must be within the field dimensions.")

    if not all(isinstance(row, list) for row in field):
        raise TypeError("Field must be a 2D list.")


    path = [(end_x, end_y)]

    while path[-1] != (start_x, start_y):
        x, y = path[-1]

        min_value = float('inf')
        next_step = None

        # Check each neighboring cell (up, down, left, right)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            # Check if the neighbor is within bounds
            if 0 <= nx < len(field) and 0 <= ny < len(field[0]):
                neighbor_value = field[nx][ny]

                # Check for 'S' as a valid next step
                if neighbor_value == 'S':
                    next_step = (nx, ny)
                    break

                # Choose the neighbor with the smallest value but greater than 0
                elif isinstance(neighbor_value, int) and 0 < neighbor_value < min_value:
                    min_value = neighbor_value
                    next_step = (nx, ny)

        # If a next step is found, add it to the path
        if next_step:
            path.append(next_step)
        else:
            # No valid path found, break the loop
            print("No valid path found.")
            break

    # Reversing the path list so it starts from start -> end
    path.reverse()

    # Visualize the path on the field
    fu.visualise_path(field, path)


    return field
