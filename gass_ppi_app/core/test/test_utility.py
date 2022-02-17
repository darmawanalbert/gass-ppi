from model.Residue import Residue
from utility.is_same_residue import is_same_residue

class TestUtility:
    def test_is_same_residue(self):
        sample_residue_1 = Residue("ASP", 1, "L", "CG", [-1,-1,-1], 0.0)
        sample_residue_2 = Residue("ASP", 1, "L", "CG", [-1,-1,-1], 0.0)
        assert is_same_residue(sample_residue_1, sample_residue_2) == True

