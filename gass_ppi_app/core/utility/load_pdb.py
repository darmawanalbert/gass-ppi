def load_pdb(pdb_id, pdb_directory_path, pdb_parser, lha_dict, reference_atom="lha"):
    """Load PDB
    Given a PDB ID and its directory, load the .pdb file using Bio.PDB module and generate a list of residue

    Parameters:
    pdb_id (str): The PDB ID for the protein structure
    pdb_directory_path (str): Absolute path to access the PDB file
    pdb_parser (Bio.PDB.PDBParser.PDBParser): Bio.PDB Parser
    lha_dict (dict{residue_name: atom_name}): Corresponding Last Heavy Atom for each amino acids
    reference_atom (str): Reference atom used ("lha" or "ca")

    Returns:
    list[Residue]: List of Residue object which constitutes the protein structure

    """
    residue_list = []
    amino_acid_list = list(lha_dict.keys())
    pdb_file_path = pdb_directory_path + pdb_id + ".pdb"
    pdb_structure = pdb_parser.get_structure(pdb_id, pdb_file_path)

    # Calculate the SASA for each residue using Shrake-Rupley algorithm from Bio.PDB
    sr = ShrakeRupley()
    sr.compute(pdb_structure, level="R")

    # Only take the ATOM keyword (exclude the HETATM, hetero atom that is not inside standard amino acids)
    biopdb_residue_list = [residue for residue in pdb_structure.get_residues() if residue.get_resname() in amino_acid_list]
    if reference_atom == "lha":
        biopdb_atom_list = [atom for residue in biopdb_residue_list for atom in residue if atom.get_name() == lha_dict[residue.get_resname()]]
    else:
        biopdb_atom_list = [atom for residue in biopdb_residue_list for atom in residue if atom.get_name() == "CA"]

    for atom in biopdb_atom_list:
        # Create a new Residue instance
        current_residue_name = atom.get_parent().get_resname()
        current_residue_sequence_position = atom.get_parent().get_full_id()[3][1]
        current_chain_name = atom.get_parent().get_parent().id
        current_atom_name = atom.get_name()
        current_atom_coordinates = atom.get_coord().tolist()
        current_residue_sasa = float(atom.get_parent().sasa)
        current_atom = Residue(current_residue_name,
                               current_residue_sequence_position,
                               current_chain_name,
                               current_atom_name,
                               current_atom_coordinates,
                               current_residue_sasa)
        residue_list.append(current_atom)
    return residue_list

residue_3nos = load_pdb("1AHW_l_u", dbd5_path, pdb_parser, lha_dict, "lha")
print(type(residue_3nos))
print(len(residue_3nos))
for item in residue_3nos[:5]:
    print(item.residue_name)
    print(item.residue_sequence_position)
    print(item.chain_name)
    print(item.atom_name)
    print(item.atom_coordinates)
    print(item.residue_sasa)
