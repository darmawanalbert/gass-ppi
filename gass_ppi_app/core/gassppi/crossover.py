import random

def crossover(individual_1, individual_2, crossover_probability):
    """Crossover
    Given two individuals, perform a single point crossover based on crossover probability

    Parameters:
    individual_1 (list[Residue]): First parent
    individual_2 (list[Residue]): Second parent
    crossover_probability (float): The probability that a crossover occurs (between 0 and 1.0)

    Returns:
    list[Residue]: Individual 1 after crossover
    list[Residue]: Individual 2 after crossover

    """
    # Only apply crossover if a random value is within the crossover probability
    # Otherwise, simply return these individuals without performing any operation
    random_percentage = random.random()
    if random_percentage < crossover_probability:
        # Randomly determine the crossover point
        individual_size = len(individual_1)
        crossover_point = random.randrange(individual_size)

        # Swap residues between two individuals, starting from the crossover point
        for i in range(crossover_point, individual_size):
            individual_1[i], individual_2[i] = individual_2[i], individual_1[i]

    return (individual_1, individual_2)
