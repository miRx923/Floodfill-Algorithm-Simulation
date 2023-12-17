""" File containing field utilities to work with field """

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


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



def print_field_using_plot(field):
    """ Function for printing the final field with plot """

    rows = len(field)
    cols = len(field[0])

    # Map characters and numbers to numerical values
    # Create a new array of zeros with the same shape
    mapped_array = np.zeros_like(field, dtype=float)  

    # Constants for the special characters
    NUMBER_VALUE = 1
    E_VALUE = 2
    S_VALUE = 3
    STAR_VALUE = 4

    for i, row in enumerate(field):
        for j, item in enumerate(row):
            if item == 'S':
                mapped_array[i][j] = S_VALUE
            elif item == 'E':
                mapped_array[i][j] = E_VALUE
            elif item == '*':
                mapped_array[i][j] = STAR_VALUE
            else:
                mapped_array[i][j] = NUMBER_VALUE

    # Create a custom color map
    cmap = ListedColormap(['gray', 'red', 'green', 'blue'])  # gray for numbers, green for 'S', red for 'E', blue for '*'

    # Plotting
    plt.figure(figsize=(rows, cols))
    plt.imshow(mapped_array, cmap=cmap)
    plt.title('Floodfill plot visualisation')
    plt.xticks(np.arange(mapped_array.shape[1]))
    plt.yticks(np.arange(mapped_array.shape[0]))
    plt.show()
