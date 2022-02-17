def is_residue_in_interface(residue, interface):
    """Is Residue In Interface
    Given a residue object and an interface, check whether this residue object exists inside the interface

    Parameters:
    residue (Residue): A Residue object to be checked
    interface (list[Residue]): List of Residue objects which represents a protein interface

    Returns:
    bool: A value which indicates whether the residue exists inside the interface

    """
    return any([True if is_same_residue(residue, current_residue) else False for current_residue in interface])
