import random

def generate_initial_population(input_protein_structure, interface_template, population_size):
    """Generate Initial Population
    Given the input protein structure and its interface template, generate list
    of random individuals which constitutes the initial population.

    Each residue inside the individual needs to have the same residue_name compared to
    the interface_template, but can have different residue_sequence_position or chain_name.

    Parameters:
    input_protein_structure (list[Residue]): List of Residues object which constitutes the input protein structure
    interface_template (list[Residue]): List of Residue object which constitutes the interface template
    population_size (int): The number of random individuals to be generated

    Returns:
    list[list[Residue]]: The initial population (list of individuals)

    """

    # Split the input_protein_structure into 20 list (based on amino_acid_list)
    input_protein_dict= { x: [] for x in amino_acid_list }
    for residue in input_protein_structure:
        input_protein_dict[residue.residue_name].append(residue)

    initial_population_list = []
    # Generate the initial population
    for _ in range(population_size):
        # Generate a random individual
        random_individual = []
        for residue in interface_template:
            amino_acid_type = residue.residue_name
            # Generate a random residue that aligns with the amino_acid_type
            if len(input_protein_dict[amino_acid_type]) > 0:
                random_residue_index = random.randrange(len(input_protein_dict[amino_acid_type]))
                random_residue = input_protein_dict[amino_acid_type][random_residue_index]
                # Ensure that the randomly picked residue is distinct inside the same individual
                while is_residue_in_interface(random_residue, random_individual):
                    random_residue_index = random.randrange(len(input_protein_dict[amino_acid_type]))
                    random_residue = input_protein_dict[amino_acid_type][random_residue_index]
            else:
                # In case the protein structure doesn't contain the required amino_acid_type, select any random residue with any type
                random_residue_index = random.randrange(len(input_protein_structure))
                random_residue = input_protein_structure[random_residue_index]

            random_individual.append(random_residue)
        initial_population_list.append(random_individual)

    return initial_population_list
