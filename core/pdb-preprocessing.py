'''
Script that generates a complete .txt file from a .pdb file.
Saves name, ec number, UniProt, and resolution information.
All AC or LHA atoms of all protein residues are saved.
The script runs in 3 ways:
- If it runs without any arguments, it generates txt file from all pdb files in the current directory;
- If you put 1 argument, it's the directory you want to run in for all pdb;
- If you put 2 arguments, it's run to the directory you want and to which specific pdb.

caminho == path

'''

import os
import sys

dict_lha = {"ALA":"CB", "ARG":"CZ", "ASN":"CG", "ASP":"CG", "CYS":"SG", "GLN":"CD", "GLU":"CD", "GLY":"CA", "HIS":"CE1", "ILE":"CD1", "LEU":"CD1", "LYS":"NZ", "MET":"CE", "PHE":"CZ", "PRO":"CG", "SER":"OG", "THR":"CG2", "TRP":"CH2", "TYR":"OH", "VAL":"CG1"}

list_pdbs = []
if len(sys.argv) == 1:
    caminho = ""
    arq_dir = os.listdir()

elif len(sys.argv) == 2:
    caminho = sys.argv[1]
    arq_dir = os.listdir(caminho)

elif len(sys.argv) == 3:
    caminho = sys.argv[1]
    arq_dir = os.listdir(caminho)
    list_pdbs.append(sys.argv[2])

else:
    print("Invalid arguments!")
    exit()

if len(sys.argv) != 3:
    for a in arq_dir:
        if '.pdb' in a and len(a) == 8:
            list_pdbs.append(a)

if not list_pdbs:
    print("There are no PDB files in the directory!")
    exit()
cont = 1

# while(1):
#     reference_atom = input("Plase insert the reference atom (CA or LHA): ").upper().strip()
#     if reference_atom == 'CA' or reference_atom == 'LHA':
#         break
#     else:
#         print("Provided reference atom is not valid. Please choose beetween CA or LHA.\n")

reference_atom = 'LHA'

for nome_pdb in list_pdbs:
    print("{}: {}".format(cont, nome_pdb))
    cont = cont + 1
    arq_pdb = open(caminho + nome_pdb, 'r')
    linhas_pdb = arq_pdb.readlines()
    pdb_lines = linhas_pdb
    linhas_pdb = [linha.replace('\n', '') for linha in linhas_pdb]
    nome_txt = nome_pdb[:-4] + '_lha.pdb'
    arq_txt = open(caminho + nome_txt, 'w')
    ec_proteina = 'NULL'
    unp_proteina = 'NULL'
    for l_pdb in linhas_pdb:
        if l_pdb.find('HEADER') != -1 and len(l_pdb.strip().split()[-1]) == 4:
            nome_proteina = l_pdb.strip().split()[-1]
        if l_pdb.find('EC:') != -1 and l_pdb.find('COMPND') != -1:
            ec_proteina = l_pdb.strip().split()[-1].replace(';', '')
        if l_pdb.find('UNP') != -1 and l_pdb.find('DBREF') != -1:
            unp_proteina = l_pdb.strip().split()[6]
        if l_pdb.find('RESOLUTION.') != -1 and l_pdb.find('REMARK') != -1:
            reso_proteina = l_pdb.strip().split()[3]
    arq_txt.write(nome_proteina)
    arq_txt.write('\n')
    arq_txt.write(ec_proteina)
    arq_txt.write('\n')
    arq_txt.write(unp_proteina)
    arq_txt.write('\n')
    arq_txt.write(reso_proteina)
    arq_txt.write('\n')
    arq_pdb.close()

    # loops that run through all CA or LHA atoms and check for duplicate data
    for i in range(0,len(pdb_lines)):
        encontrou = False
        if pdb_lines[i][0:4] == 'ATOM':
            res = pdb_lines[i][17:20]
            #print(res)
            if reference_atom == 'CA':
                ra = 'CA'
            else:
                ra = dict_lha[res]
            if pdb_lines[i][12:16].strip() == ra:
                for j in range(i+1,len(pdb_lines)):
                    if pdb_lines[j][0:4] == 'ATOM' and pdb_lines[j][12:16].strip() == ra:
                        if pdb_lines[i][21:22] == pdb_lines[j][21:22] and pdb_lines[i][22:26].strip() == pdb_lines[j][22:26].strip():
                            encontrou = True
                if encontrou == False:
                    if pdb_lines[i][16] != " ":
                        linhas_pdb[i] = linhas_pdb[i][:16] + " " + linhas_pdb[i][17:]
                    arq_txt.write("%s\n" % linhas_pdb[i])

    arq_txt.close()
