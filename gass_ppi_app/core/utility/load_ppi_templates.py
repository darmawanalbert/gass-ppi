import json
from model.Residue import Residue

def load_ppi_templates(load_directory_path, file_name):
    """Load PPI Templates
    Using Python JSON library, load a JSON file which contains PPI templates dictionary

    Parameters:
    load_directory_path (str): Absolute directory path to load the file
    file_name (str): The file name with its .json extension to be loaded

    Returns:
    dict{pdb_id: list[Residue]}: Dictionary of PPI templates for each PDB ID

    """
    # In case the file is empty, initialize an empty dictionary to be returned
    deserialized_ppi_templates = {}

    # Load the file
    with open(load_directory_path + file_name, "r") as fp:
        loaded_ppi_templates = json.load(fp)

    # Deserialized the loaded_ppi_templates
    deserialized_ppi_templates = { pdb_id: [Residue(x['residue_name'], x['residue_sequence_position'], x['chain_name'], x['atom_name'], x['atom_coordinates'], x['residue_sasa']) for x in residue_list]
                                    for pdb_id, residue_list in loaded_ppi_templates.items() }
    return deserialized_ppi_templates
