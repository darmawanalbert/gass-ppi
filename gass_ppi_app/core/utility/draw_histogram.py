import matplotlib.pyplot as plt

def draw_histogram(data, title, x_label, y_label):
    """
    Given x_axis data and additional information, draw and show a histogram using matplotlib

    Parameters:
    data (list): List of x_axis values
    title (str): Histogram title
    x_label (str): Horizontal label
    y_label (str): Vertical label

    Returns:
    None

    """
    plt.hist(data, bins="auto")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(axis="y", alpha=0.75)
    plt.show()
