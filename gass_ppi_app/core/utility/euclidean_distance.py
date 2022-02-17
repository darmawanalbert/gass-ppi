import numpy as np

def euclidean_distance(coordinate_1, coordinate_2):
    """Euclidean Distance
    Given 3-dimensional coordinates of 2 atoms, calculate its Euclidean distance

    Parameters:
    coordinate_1 (list[float]): x,y,z coordinates of the first atom
    coordinate_2 (list[float]): x,y,z coordinates of the second atom

    Returns:
    float: The euclidean distance

    """
    return float(np.sqrt(((coordinate_1[0] - coordinate_2[0]) ** 2) +
                   ((coordinate_1[1] - coordinate_2[1]) ** 2) +
                   ((coordinate_1[2] - coordinate_2[2]) ** 2)))
