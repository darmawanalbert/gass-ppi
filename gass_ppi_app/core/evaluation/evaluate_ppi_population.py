from evaluation.evaluate_ppi import evaluate_ppi

def evaluate_ppi_population(actual_interface, population_list, protein_structure, ranking_size=1):
    """Evaluate PPI Population
    Given a population of PPI produced by GASS-PPI method, evaluate n individual
    (where n is the ranking_size) using evaluate_ppi method and return the best individual.
    For now, the "best" is indicated by the highest MCC

    Parameters:
    actual_interface (list[Residue]): List of Residue objects which represents the experimentally proven interface
    population_list (list[(list[Residue], float)]): The population list to be evaluated (already sorted in GASS-PPI)
    protein_structure (list[Residue]): List of Residue objects which represents the entire protein structure
    ranking_size (int): Number of individuals to be evaluated (from individual #0 to #ranking_size-1)


    Returns:
    int: Best Individual Ranking (from 0 to population_size - 1)
    float: Precision (Positive Predictive Value) score
    float: Recall (Sensitivity/True Positive Rate) score
    float: AUC-ROC score
    float: AUC-PR score
    float: Matthew's Correlation Coefficient score
    float: Specificity (True Negative Rate) score
    float: NPV (Negative Predictive Value) score

    """
    max_ranking = 0
    max_precision = 0.0
    max_recall = 0.0
    max_auc_roc = 0.0
    max_auc_pr = 0.0
    max_mcc = 0.0
    max_specificity = 0.0
    max_npv = 0.0

    # Evaluate each individual until reaching the ranking_size
    for i in range(ranking_size):
        precision, recall, auc_roc, auc_pr, mcc, specificity, npv = evaluate_ppi(actual_interface, population_list[i][0], protein_structure)
        # Check whether the MCC is higher than the previousn individual
        if mcc > max_mcc:
            max_ranking = i
            max_precision = precision
            max_recall = recall
            max_auc_roc = auc_roc
            max_auc_pr = auc_pr
            max_mcc = mcc
            max_specificity = specificity
            max_npv = npv

    return (max_ranking, max_precision, max_recall, max_auc_roc, max_auc_pr, max_mcc, max_specificity, max_npv)