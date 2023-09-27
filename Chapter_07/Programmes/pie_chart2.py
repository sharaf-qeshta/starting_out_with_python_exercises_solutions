# This program displays a simple pie chart.
import matplotlib.pyplot as plt


def main():
    # Create a list of sales amounts.
    sales = [100, 400, 300, 600]

    # Create a list of labels for the slices.
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

    # Create a pie chart from the values.

    plt.pie(sales, labels=slice_labels)

    # Add a title.
    plt.title('Sales by Quarter')

    # Display the pie chart.
    plt.show()


# Call the main function.
main()
