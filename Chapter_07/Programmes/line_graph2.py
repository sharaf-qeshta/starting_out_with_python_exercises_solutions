# This program displays a simple line graph.
import matplotlib.pyplot as plt


def main():
    # Create lists with the X and Y coordinates of each data point.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Build the line graph.
    plt.plot(x_coords, y_coords)

    # Add a title.
    plt.title('Sample Data')

    # Add labels to the axes.
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')

    # Add a grid.
    plt.grid(True)

    # Display the line graph.
    plt.show()


# Call the main function.
main()
