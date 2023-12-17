""" File containing field utilities to work with field """


def initialise_field(x_field_size, y_field_size, start_x, start_y, end_x, end_y):
    """ Function for initialising blank field """
    # Field initialization and filling it with zeros
    field = [[0 for _ in range(x_field_size)] for _ in range(y_field_size)]

    # Set the starting and the end point in the field
    field[start_x][start_y] = 'S'  # Start is represented by letter S
    field[end_x][end_y] = 'E'      # End is represented by letter E

    return field



def visualise_path(field, path):
    """ Function to visualise the shortest path in the filled field """
    for x, y in path:
        if field[x][y] != 'S' and field[x][y] != 'E':
            field[x][y] = '*'


    return field



def print_field_in_terminal(field):
    """ Function to print the field in the terminal """
    print()
    print('\n'.join([' '.join(['{:<4}'.format(str(item)) for item in row]) for row in field]))
    print()
