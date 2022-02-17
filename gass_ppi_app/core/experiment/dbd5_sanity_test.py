from utility.load_ppi_templates import load_ppi_templates
from utility.constant import templates_path
from evaluation.evaluate_dbd5 import evaluate_dbd5
from utility.dbd5_constant import dbd5_ei_list, dbd5_es_list, dbd5_er_list, dbd5_a_list, dbd5_ab_list, dbd5_og_list, dbd5_or_list, dbd5_ox_list

# Load a PPI template dictionary from .json files (to be used in the main program)
a_templates_dict = load_ppi_templates(templates_path, "dbd5_a_templates.json")
ei_templates_dict = load_ppi_templates(templates_path, "dbd5_ei_templates.json")
er_templates_dict = load_ppi_templates(templates_path, "dbd5_er_templates.json")
es_templates_dict = load_ppi_templates(templates_path, "dbd5_es_templates.json")
ab_templates_dict = load_ppi_templates(templates_path, "dbd5_ab_templates.json")
og_templates_dict = load_ppi_templates(templates_path, "dbd5_og_templates.json")
ox_templates_dict = load_ppi_templates(templates_path, "dbd5_ox_templates.json")
or_templates_dict = load_ppi_templates(templates_path, "dbd5_or_templates.json")

all_templates_dict = {**a_templates_dict, **ei_templates_dict, **er_templates_dict,
                      **es_templates_dict, **ab_templates_dict, **og_templates_dict,
                      **ox_templates_dict, **or_templates_dict}
print(len(all_templates_dict))

print("DBD5: Enzyme-Inhibitor (EI)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_ei_list[:5], ei_templates_dict, sanity_test=True, verbose=True)
print("\n\n")

print("DBD5: Enzyme-Substrate (ES)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_es_list[:5], es_templates_dict, sanity_test=True, verbose=True)
print("\n\n")

print("DBD5: Enzyme complex with a regulatory or accessory chain (ER)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_er_list[:5], er_templates_dict, sanity_test=True, verbose=True)
print("\n\n")

print("DBD5: Antibody-Antigen (A)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_a_list[:5], a_templates_dict, sanity_test=True, verbose=True)
print("\n\n")

print("DBD5: Antigen-Bound Antibody (AB)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_ab_list[:5], ab_templates_dict, sanity_test=True, verbose=True)
print("\n\n")

print("DBD5: Others, G-protein containing (OG)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_og_list[:5], og_templates_dict, sanity_test=True, verbose=True)
print("\n\n")

print("DBD5: Others, Receptor containing (OR)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_or_list[:5], or_templates_dict, sanity_test=True, verbose=True)
print("\n\n")

print("DBD5: Others, miscellaneous (OX)")
_, _, _, _, _, _, _, _ = evaluate_dbd5(dbd5_ox_list[:5], ox_templates_dict, sanity_test=True, verbose=True)
print("\n\n")