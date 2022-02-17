class Residue:
    """
    A class to represent a Residue.
    In this case, a Residue is represented by a reference atom (either LHA, CA, etc).
    Residue is the "gene" in genetic algorithms (which constitutes an "individual").
    In other words, an individual is a list of Residue.
    A residue consists of 2 residue information, 1 chain information, and 2 reference atom information

    Attributes
    ----------
    residue_name : str
        The 3-letter amino acid name
        Example: "LYS"

    residue_sequence_position: int
        The position number of this residue inside the whole protein sequence
        Example: 67

    chain_name : str
        The 1-letter name of the corresponding chain
        Example: "A"

    atom_name : str
        The abbreviation of the reference atom name
        Example: "CA"

    atom_coordinates : list[float]
        The 3-dimensional coordinates of the reference atom
        Example: [-7.555, 8.098, 13.093]

    residue_sasa : float
        The Solvent Accessibility Surface Areas (SASA) associated for each residue
        Calculated using Shrake-Rupley algorithm. Unit in Angstrom^2
        Example: 69.11805430792289

    """
    def __init__(self, residue_name, residue_sequence_position, chain_name, atom_name, atom_coordinates, residue_sasa):
        self.residue_name = residue_name
        self.residue_sequence_position = residue_sequence_position
        self.chain_name = chain_name
        self.atom_name = atom_name
        self.atom_coordinates = atom_coordinates
        self.residue_sasa = residue_sasa
