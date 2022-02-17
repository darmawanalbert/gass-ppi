import random

def mutation(input_protein_structure, individual, mutation_probability):
    """Mutation
    Given an individual, perform a single point mutations based on mutation probability.
    In this case, no conservative mutation is employed

    Parameters:
    input_protein_structure (list[Residue]): List of Residues object which constitutes the input protein structure
    individual (list[Residue]): Individual to be mutated
    mutation_probability (float): The probability that a mutation occurs (between 0 and 1.0)

    Returns:
    list[Residue]: Mutated individuals

    """
    # Only apply mutation if a random value is within the mutation probability
    # Otherwise, simply return the individual without performing any operation
    random_percentage = random.random()
    if random_percentage < mutation_probability:
        # Randomly determine the mutation point
        individual_size = len(individual)
        mutation_point = random.randrange(individual_size)
        mutated_residue = individual[mutation_point]

        # Mutate the residue at the mutation point into the same amino acid types
        possible_mutation = [residue for residue in input_protein_structure
                            if residue.residue_name == mutated_residue.residue_name
                            and residue.residue_sequence_position != mutated_residue.residue_sequence_position]

        if len(possible_mutation) > 0:
            new_residue_index = random.randrange(len(possible_mutation))
            new_residue = possible_mutation[new_residue_index]
            individual[mutation_point] = new_residue

    return individual
