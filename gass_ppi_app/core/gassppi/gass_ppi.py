def gass_ppi(input_protein_structure, interface_template, population_size=150, number_of_generations=100, crossover_probability=0.9, mutation_probability=0.9, tournament_size=2, number_of_tournament=50):
    """GASS-PPI Method
    Given the input protein structure and the interface template, perform genetic algorithms
    to search the most likely interface

    Parameters:
    input_protein_structure (list[Residue]): List of Residue which constitutes the entire protein structure
    interface_template (list[Residue]): List of Residue which is used as a template for the genetic algorithms
    population_size (int): Total number of individuals inside the population
    number_of_generations (int): Number of iterations run in the genetic algorithm
    crossover_probability (float): Probability value between 0-1 which governs the likelihood that crossover is performed
    mutation_probability (float): Probability value between 0-1 which governs the likelihood that mutation is performed
    tournament_size (int): The number of individuals inside a particular tournament
    number_of_tournament (int): Number of tournaments to be performed

    Returns:
    list[(list[Residue], float)]: The final population generated from the genetic algorithms.
                                  Each tuple consists of the individual and its correspondings fitness score

    """
    template_size = len(interface_template)
    protein_structure = list(input_protein_structure)

    # Initial Population
    population_list_no_fitness = generate_initial_population(protein_structure, interface_template, population_size)
    population_list = [(individual, calculate_fitness_score(individual, interface_template)) for individual in population_list_no_fitness]

    # Evolutionary Steps
    for i in range(number_of_generations):
        # Selection
        parent_list = deterministic_tournament_selection(population_list, tournament_size, number_of_tournament)

        for j in range(0, len(parent_list), 2):
            # Crossover
            new_individual_1, new_individual_2 = crossover(population_list[j][0], population_list[j+1][0], crossover_probability)

            # Mutation
            mutated_new_individual_1 = mutation(protein_structure, new_individual_1, mutation_probability)
            mutated_new_individual_2 = mutation(protein_structure, new_individual_2, mutation_probability)

            # Fitness Evaluation
            fitness_score_1 = calculate_fitness_score(mutated_new_individual_1, interface_template)
            fitness_score_2 = calculate_fitness_score(mutated_new_individual_2, interface_template)

            # Add 2 new individuals into the population_list
            population_list.append((mutated_new_individual_1, fitness_score_1))
            population_list.append((mutated_new_individual_2, fitness_score_2))

        # Population Management (steady-state)
        population_list.sort(key = lambda x: x[1])
        population_list = population_list[:population_size]

    return population_list
