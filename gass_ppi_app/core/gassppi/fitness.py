import numpy as np
from model.Residue import Residue
from utility.euclidean_distance import euclidean_distance

def calculate_fitness_score(individual, interface_template):
    """Calculate Fitness Score
    Adhering to the original GASS, calculate the spatial LHA distance between an individual and the interface template
    Essentially, it's the modified version of RMSD

    Parameters:
    individual (list[Residue]): The individual that needs to be evaluated
    interface_template (list[Residue]): The interface template, used as a reference

    Returns:
    float: The fitness score of an individual

    """
    n = len(individual)

    individual_coordinates_list = [residue.atom_coordinates for residue in individual]
    individual_distance_list = [euclidean_distance(individual_coordinates_list[i], individual_coordinates_list[j]) for i in range(n-1) for j in range(i+1, n)]

    template_coordinates_list = [residue.atom_coordinates for residue in interface_template]
    template_distance_list = [euclidean_distance(template_coordinates_list[i], template_coordinates_list[j]) for i in range(n-1) for j in range(i+1, n)]

    fitness_score = float(np.sqrt(np.sum([(abs(x[0] - x[1]) ** 2) for x in zip(individual_distance_list, template_distance_list)])))
    return fitness_score

# Sanity Test (based on the image above)
individual_3e7s = [Residue("CYS", 98, "A", "SG", [15.188, 51.16, 29.614], 0.0),
                   Residue("CYS", 93, "B", "SG", [18.566, 50.223, 29.192], 0.0),
                   Residue("CYS", 93, "A", "SG", [16.816, 52.802, 26.558], 0.0),
                   Residue("CYS", 98, "B", "SG", [16.029, 49.192, 26.545], 0.0)]

template_3nos = [Residue("CYS", 99, "A", "SG", [19.639, 1.17, 43.588], 0.0),
                 Residue("CYS", 94, "B", "SG", [17.385, -1.714, 43.236], 0.0),
                 Residue("CYS", 94, "A", "SG", [20.732, -1.688, 41.537], 0.0),
                 Residue("CYS", 99, "B", "SG", [17.848, 0.685, 40.313], 0.0)]

test_fitness_score = calculate_fitness_score(individual_3e7s, template_3nos)
test_fitness_score