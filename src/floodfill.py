""" File for Floodfill algorithm in Python using terminal visualisation """

import field_utils as fu


def flood_fill(x_field_size, y_field_size, start_x, start_y, end_x, end_y):
    """Function for filling numbers in the field"""

    # Error checking
    if not all(isinstance(i, int) for i in [x_field_size, y_field_size, start_x, start_y, end_x, end_y]):
        raise TypeError("All parameters must be integers.")

    if x_field_size <= 0 or y_field_size <= 0:
        raise ValueError("x_field_size and y_field_size must be greater than 0.")

    if start_x < 0 or start_x >= x_field_size or start_y < 0 or start_y >= y_field_size:
        raise ValueError("start_x and start_y must be within the x_field_size and y_field_size.")

    if end_x < 0 or end_x >= x_field_size or end_y < 0 or end_y >= y_field_size:
        raise ValueError("end_x and end_y must be within the x_field_size and y_field_size.")


    field = fu.initialise_field(x_field_size, y_field_size, start_x, start_y, end_x, end_y)

    # Printing blank field
    fu.print_field_in_terminal(field)

    # Flood fill algorithm
    number = 1
    to_fill = [(start_x, start_y)]

    while to_fill:
        next_fill = []

        for x, y in to_fill:

            # Check each neighboring cell (up, down, left, right)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy

                # Check if the neighbor is within bounds and not already filled
                if ((0 <= nx < y_field_size) and (0 <= ny < x_field_size) and (field[nx][ny] == 0)):
                    field[nx][ny] = number
                    next_fill.append((nx, ny))

        to_fill = next_fill
        number += 1

    return field
