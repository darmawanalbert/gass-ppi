import random

def deterministic_tournament_selection(population_list, tournament_size, number_of_tournament):
    """Deterministic Tournament Selection
    Perform deterministic tournament selection towards current population list
    to select parents (for generating new generations)

    Parameters:
    population_list (list[(list[Residue], int)]): Current list of population
    tournament_size (int): Hyperparameter to determine how many random individuals in each tournament
    number_of_tournament (int): Hyperparameter to determine how many tournaments to be performed

    Returns:
    list[list[Residue]]: List of parents

    """
    random.shuffle(population_list)

    parent_list = []
    # Perform n tournaments (where n is the number_of_tournament)
    for _ in range(number_of_tournament):
        # Choose random individuals to participate in the tournament
        tournament_participant_list = []
        for _ in range(tournament_size):
            random_idx = random.randrange(len(population_list))
            tournament_participant_list.append(population_list[random_idx])
        # Find the fittest individual from the tournament_participant_list
        fittest_individual = tournament_participant_list[0]
        for i in range(1, len(tournament_participant_list)):
            if tournament_participant_list[i][1] < fittest_individual[1]:
                fittest_individual = tournament_participant_list[i]

        parent_list.append(fittest_individual)

    return parent_list
