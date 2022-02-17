from model.Residue import Residue

def is_same_residue(residue_1, residue_2):
    """Is Same Residue
    Given two Residue objects, determine whether it is the same residue or not

    Parameters:
    residue_1 (Residue): The first residue to be compared
    residue_2 (Residue): The second residue to be compared

    Returns:
    bool: A value which indicates whether these two Residue objects are the same or not
    """

    # For now, two residues are the same if the residue_name, residue_sequence_position,
    # and the chain_name are the same.
    # Regardless whether it is the same instance or not
    is_same_residue_name = residue_1.residue_name == residue_2.residue_name
    is_same_sequence_position = residue_1.residue_sequence_position == residue_2.residue_sequence_position
    is_same_chain_name = residue_1.chain_name == residue_2.chain_name

    return (is_same_residue_name and is_same_sequence_position and is_same_chain_name)
