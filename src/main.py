""" Main file for floodfill algorithm """

import floodfill as ff
import shortest_path as sp
import field_utils as fu


if __name__ == "__main__":

    # Executes the flood fill algorithm
    field = ff.flood_fill(x_field_size = 10, y_field_size = 10, start_x = 1, start_y = 1, end_x = 7, end_y = 7)
    # Printing the field after executing floodfill algorithm
    fu.print_field_in_terminal(field)

    # Finds shortest path in the filled field
    shortest_path_field = sp.find_shortest_path(field, 1, 1, 7, 7)
    # Printing the field with the path visualized
    fu.print_field_in_terminal(shortest_path_field)
    
    # Printing the field with the path visualised using plot
    fu.print_field_using_plot(shortest_path_field)
