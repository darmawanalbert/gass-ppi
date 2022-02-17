import numpy as np
from utility.load_pdb import load_pdb
from utility.draw_histogram import draw_histogram
from gassppi.verification import can_run_gass_ppi
from gassppi.gass_ppi import gass_ppi
from evaluation.evaluate_ppi_population import evaluate_ppi_population

def evaluate_dbd5(pdb_id_list, templates_dict, sanity_test=False, ranking_size=100, verbose=False):
    """Evaluate DBD5
    Given a list of PDB ID available in Docking Benchmark 5 and precomputed PPI templates,
    execute GASS-PPI on each protein and evaluate the performance

    Parameters:
    pdb_id_list (list[str]): List of PDB ID available in Docking Benchmark 5
    ppi_templates_dict (dict{pdb_id: list[Residue]}): Dictionary of PPI templates for each PDB ID
    sanity_test (bool): True for sanity test (using its own template), False otherwise (using multiple templates)
    ranking_size (int): Number of individuals to be evaluated (from individual #0 to #ranking_size-1)
    verbose (bool): True for additional logs, False otherwise

    Returns:
    list[int]: Individual ranking list
    list[float]: List of precision score
    list[float]: List of recall score
    list[float]: List of AUC-ROC score
    list[float]: List of AUC-PR score
    list[float]: List of MCC score
    list[float]: List of Specificity score
    list[float]: List of NPV score

    """
    ligand_pdb_id_list = [pdb_id + "_l_u" for pdb_id in pdb_id_list]
    receptor_pdb_id_list = [pdb_id + "_r_u" for pdb_id in pdb_id_list]

    individual_ranking_list = []
    precision_list = []
    recall_list = []
    auc_roc_list = []
    auc_pr_list = []
    mcc_list = []
    specificity_list = []
    npv_list = []

    # For each PDB ID, evaluate both its corresponding ligand and receptor
    for idx in range(len(pdb_id_list)):
        # LIGAND
        # Step 1: Load the ligand's protein structure and PPI template
        ligand_pdb_id = ligand_pdb_id_list[idx]
        ligand_pdb_structure = load_pdb(ligand_pdb_id, dbd5_path, pdb_parser, lha_dict, "lha")

        ligand_interface_template = templates_dict[ligand_pdb_id]
        if sanity_test:
            ligand_interface_template = templates_dict[ligand_pdb_id]

        # Step 2: GASS-PPI
        if can_run_gass_ppi(ligand_pdb_structure, ligand_interface_template):
            ligand_predicted_population_list = gass_ppi(ligand_pdb_structure, ligand_interface_template)

            # Step 3: Evaluation
            ligand_actual_interface = templates_dict[ligand_pdb_id]
            individual_ranking, precision, recall, auc_roc, auc_pr, mcc, specificity, npv = evaluate_ppi_population(ligand_actual_interface, ligand_predicted_population_list, ligand_pdb_structure, ranking_size)
            individual_ranking_list.append(individual_ranking)
            precision_list.append(precision)
            recall_list.append(recall)
            auc_roc_list.append(auc_roc)
            auc_pr_list.append(auc_pr)
            mcc_list.append(mcc)
            specificity_list.append(specificity)
            npv_list.append(npv)
        else:
            print("Cannot run GASS-PPI on ", ligand_pdb_id)
            precision_list.append(0)
            recall_list.append(0)
            auc_roc_list.append(0)
            auc_pr_list.append(0)
            mcc_list.append(0)
            specificity_list.append(0)
            npv_list.append(0)

        # RECEPTOR
        # Step 1: Load the receptor's protein structure and PPI template
        receptor_pdb_id = receptor_pdb_id_list[idx]
        receptor_pdb_structure = load_pdb(receptor_pdb_id, dbd5_path, pdb_parser, lha_dict, "lha")

        receptor_interface_template = templates_dict[receptor_pdb_id]
        if sanity_test:
            receptor_interface_template = templates_dict[receptor_pdb_id]

        # Step 2: GASS-PPI
        if can_run_gass_ppi(receptor_pdb_structure, receptor_interface_template):
            receptor_predicted_population_list = gass_ppi(receptor_pdb_structure, receptor_interface_template)

            # Step 3: Evaluation
            receptor_actual_interface = templates_dict[receptor_pdb_id]
            individual_ranking, precision, recall, auc_roc, auc_pr, mcc, specificity, npv = evaluate_ppi_population(receptor_actual_interface, receptor_predicted_population_list, receptor_pdb_structure, ranking_size)
            individual_ranking_list.append(individual_ranking)
            precision_list.append(precision)
            recall_list.append(recall)
            auc_roc_list.append(auc_roc)
            auc_pr_list.append(auc_pr)
            mcc_list.append(mcc)
            specificity_list.append(specificity)
            npv_list.append(npv)
        else:
            print("Cannot run GASS-PPI on ", receptor_pdb_id)
            precision_list.append(0)
            recall_list.append(0)
            auc_roc_list.append(0)
            auc_pr_list.append(0)
            mcc_list.append(0)
            specificity_list.append(0)
            npv_list.append(0)

    # Additional logs for development purposes
    if verbose:
        draw_histogram(individual_ranking_list, "Best Individual Ranking for each monomer", "Individual Ranking", "Frequency")
        print("Mean Precision: ", np.mean(precision_list))
        print("Mean Recall: ", np.mean(recall_list))
        print("Mean AUC-ROC Score: ", np.mean(auc_roc_list))
        print("Mean AUC-PR Score: ", np.mean(auc_pr_list))
        print("Mean MCC: ", np.mean(mcc_list))
        print("Mean Specificity: ", np.mean(specificity_list))
        print("Mean NPV: ", np.mean(npv_list))

    return (individual_ranking_list, precision_list, recall_list, auc_roc_list, auc_pr_list, mcc_list, specificity_list, npv_list)
