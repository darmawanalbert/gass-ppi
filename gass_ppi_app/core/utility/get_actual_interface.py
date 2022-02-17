from utility.euclidean_distance import euclidean_distance
from utility.load_pdb import load_pdb

def get_actual_interface(residue_list_1, residue_list_2, distance_threshold=6.0):
    """Get Actual Interface
    Given one receptor structure and one ligand structure, infer its interfaces based on certain distance threshold

    Parameters:
    residue_list_1 (list[Residue]): List of Residue object from the first protein structure
    residue_list_2 (list[Residue]): List of Residue object from the second protein structure
    distance_threshold (float): The acceptable distance between a receptor's atom and a ligand's atom (in Angstrom unit)

    Returns:
    list[Residue]: List of Residue object which constitutes the protein interface

    """
    interface_list = []
    for residue_1 in residue_list_1:
        for residue_2 in residue_list_2:
            current_distance = euclidean_distance(residue_1.atom_coordinates, residue_2.atom_coordinates)
            if current_distance < distance_threshold:
                interface_list.append(residue_1)
                break

    return interface_list

ligand = load_pdb("1AHW_l_u", dbd5_path, pdb_parser, lha_dict, "lha")
receptor = load_pdb("1AHW_r_u", dbd5_path, pdb_parser, lha_dict, "lha")
sample_interface_list = get_actual_interface(ligand, receptor, 5.0)
print(sample_interface_list)
print(type(sample_interface_list))
print(len(sample_interface_list))
for item in sample_interface_list:
    print(item.residue_name)
