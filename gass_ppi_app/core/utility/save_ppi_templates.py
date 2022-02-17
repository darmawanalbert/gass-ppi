import json

def save_ppi_templates(ppi_templates_dict, save_directory_path, file_name):
    """Save PPI Templates
    Using Python JSON library, save the PPI templates dictionary as a JSON file

    Parameters:
    ppi_templates_dict (dict{pdb_id: list[Residue]}): Dictionary of PPI templates for each PDB ID
    save_directory_path (str): Absolute directory path to save the file
    file_name (str): The saved file name with its .json extension

    Returns:
    None

    """
    # Convert the ppi_templates_dict into JSON-friendly dictionary
    json_friendly_dict = { pdb_id: [residue.__dict__ for residue in residue_list] for pdb_id, residue_list in ppi_templates_dict.items() }

    # Save the file
    with open(save_directory_path + file_name, "w") as fp:
        json.dump(json_friendly_dict, fp)
