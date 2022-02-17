def tmalign_structural_alignment(pdb_id_1, pdb_id_2, pdb_directory_path, tmalign_path):
    """TMAlign Structural Alignment
    Compare structural similarities between two PDB structures (regardless of the rotation)
    https://zhanggroup.org/TM-score/

    Parameters:
    pdb_id_1 (str): The PDB ID for the first protein structure
    pdb_id_2 (str): The PDB ID for the second protein structure
    pdb_directory_path (str): Absolute path to access the PDB files
    tmalign_path (str): Absolute path to access the TMalign UNIX executable file

    Returns:
    float: The TMScore, a value between (0,1]. 1 indicates a perfect match. >0.5 is similar enough. <0.17 is two unrelated structures.

    """
    pdb_id_1_file_path = pdb_directory_path + pdb_id_1 + ".pdb"
    pdb_id_2_file_path = pdb_directory_path + pdb_id_2 + ".pdb"
    # Execute TMAlign
    tmalign_thread = subprocess.run([tmalign_path, pdb_id_1_file_path, pdb_id_2_file_path], capture_output=True, text=True)
    output_text = tmalign_thread.stdout

    # Retrieved TMScore from TMAlign results
    tmscore_raw_list = re.findall("TM-score=\s[0-9]+.[0-9]+", output_text)

    # Convert the TMScore into floats, then get the maximum TMScore
    tmscore_list = list(map(lambda x: float(re.sub("TM-score=\s", "", x)), tmscore_raw_list))
    max_tmscore = max(tmscore_list)
    return max_tmscore

tmscore = tmalign_structural_alignment("1AHW_l_u", "1BVK_l_u", dbd5_path, tmalign_path)
print(tmscore)
