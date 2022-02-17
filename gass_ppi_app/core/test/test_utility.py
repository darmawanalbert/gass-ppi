from model.Residue import Residue
from utility.is_same_residue import is_same_residue
from utility.load_pdb import load_pdb
from utility.constant import dbd5_path

class TestUtility:
    def test_is_same_residue(self):
        sample_residue_1 = Residue("ASP", 1, "L", "CG", [-1,-1,-1], 0.0)
        sample_residue_2 = Residue("ASP", 1, "L", "CG", [-1,-1,-1], 0.0)
        assert is_same_residue(sample_residue_1, sample_residue_2) == True
    def test_load_pdb(self):
        residue_3nos_list = load_pdb("1AHW_l_u", dbd5_path, "lha")
        assert len(residue_3nos_list) == 202
