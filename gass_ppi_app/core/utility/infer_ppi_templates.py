from utility.load_pdb import load_pdb
from utility.get_actual_interface import get_actual_interface

def infer_ppi_templates(pdb_id_list, pdb_directory_path, reference_atom, distance_threshold):
    """Infer PPI Templates
    For each protein complex in the dataset, calculate and infer its PPI templates

    Parameters:
    pdb_id_list (list[str]): List of Protein Complex PDB ID to be processed
    pdb_directory_path (str): Absolute path to access the PDB file
    reference_atom (str): Reference atom used ("lha" or "ca")
    distance_threshold (float): The acceptable distance between a receptor's atom and a ligand's atom (in Angstrom unit)

    Returns:
    dict{pdb_id: list[Residue]}: Dictionary of PPI templates for each PDB ID

    """
    ppi_templates_dict = {}
    for pdb_id in pdb_id_list:
        current_ligand = load_pdb(pdb_id + "_l_u", pdb_directory_path, reference_atom)
        current_receptor = load_pdb(pdb_id + "_r_u", pdb_directory_path, reference_atom)
        ppi_templates_dict[pdb_id + "_l_u"] = get_actual_interface(current_ligand, current_receptor, distance_threshold)
        ppi_templates_dict[pdb_id + "_r_u"] = get_actual_interface(current_receptor, current_ligand, distance_threshold)

    return ppi_templates_dict
