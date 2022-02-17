def print_interface_info(interface):
    """Print Interface Info
    Given an interface, print relevant information
    For debugging purpose only

    Parameters:
    interface (list[Residue]): The list of Residue object which constitutes the interface

    Returns:
    None

    """
    print("Number of Residues: ", len(interface))
    for i in range(len(interface)):
        if i > 0:
            print(" - ", end="")
        print(interface[i].residue_name, interface[i].residue_sequence_position, interface[i].chain_name, end="")
    print("")
