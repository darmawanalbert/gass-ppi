# Docking Benchmark 5.0 (abbreviated as DBD5)
# https://zlab.umassmed.edu/benchmark/benchmark5.0.html
# List of PDB ID of protein complexes based on Complex Labels
# EI = Enzyme-Inhibitor
dbd5_ei_list = [ # Rigid-body
                "1AVX", "1AY7", "1BUH", "1BVN", "1CLV", "1D6R", "1DFJ", "1EAW",
                "1EZU", "1F34", "1FLE", "1GL1", "1GXD", "1HIA", "1JTD", "1JTG",
                "1MAH", "1OPH", "1OYV", "1PPE", "1R0R", "1TMQ", "1UDI", "1YVB",
                "2ABZ", "2B42", "2J0T", "2OUL", "2SIC", "2SNI", "2UUY", "3A4S",
                "3SGQ", "3VLB", "4CPA", "4HX3", "7CEI",
                 # Medium Difficulty
                "1CGI", "1JIW", "4IZ7",
                 # Difficult
                "1ACB", "1PXV", "1ZLI", "2O3B"]

# TODO: DUPLICATE 1OYV

# ES = Enzyme-Substrate
dbd5_es_list = [ # Rigid-body
                "1E6E", "1EWY", "1Z5Y", "2A1A", "2A9K", "2MTA", "2O8V", "2OOB",
                "4H03",
                 # Medium Difficulty
                "1KKL", "1ZM4", "4LW4",
                 # Difficult
                "1F6M", "1FQ1", "1JK9", "2IDO"]
# TODO: Re-add "2PCC" to rigid-body (due to SASA calculation error)

# ER = Enzyme complex with a regulatory or accessory chain
dbd5_er_list = [ # Rigid-body
                "1F51", "1GLA", "1JWH", "1OC0", "1US7", "1WDW", "2AYO", "2GAF",
                "2OOR", "3K75", "3LVK", "3PC8",
                 # Medium Difficulty
                "1IJK", "1M10", "1NW9", "1R6Q", "2NZ8", "2Z0E" , "4FZA",
                 # Difficult
                "1JMO", "1JZD", "2OT3", "3FN1", "3H11", "4GAM"]
# TODO:L Re-add "2YVJ" to rigid-body (due to SASA calculation error)

# A = Antibody-Antigen (receptor-ligand)
dbd5_a_list = [ # Rigid-body
               "1AHW", "1BVK", "1DQJ", "1E6J", "1JPS", "1MLC", "1VFB",
               "2FD6", "2I25", "2VIS", "2VXT", "2W9E", "3EOA", "3HMX", "3MXW",
               "3RVW", "4DN4", "4FQI", "4G6J", "4G6M", "4GXU",
                # Medium Difficulty
               "3EO1", "3G6D", "3HI6", "3L5W", "3V6Z",
                # Difficult
               "1BGX"]
# TODO: Re-add "1WEJ" to rigid-body (due to SASA calculation error)

# AB = Antigen - Bound Antibody
dbd5_ab_list = [ # Rigid-body
                "1BJ1", "1FSK", "1I9R", "1IQD", "1K4C", "1KXQ", "1NCA", "1NSN",
                "1QFW", "2JEL",
                 # Difficult
                "2HMI"]

# TODO: There are two 1QFW! Investigate later

# OG = Others, G-protein containing
dbd5_og_list = [ # Rigid-body
                "1A2K", "1AZS", "1E96", "1FQJ", "1HE1", "1I4D", "1J2J", "1Z0K",
                "2FJU", "2G77", "2GTP",
                 # Medium Difficulty
                "1GP2", "1GRN", "1HE8", "1I2M", "1K5D", "1LFD", "1WQ1", "2H7V",
                "3CPH",
                 # Difficult
                "1BKD", "1IBR", "1R8S"]

# OR = Others, Receptor containing
dbd5_or_list = [ # Rigid-body
                "1GHQ", "1HCF", "1K74", "1KAC", "1KTZ", "1ML0", "1PVH", "1RV6",
                "1SBB", "1T6B", "1XU1", "1ZHH", "2AJF", "2HLE", "2X9A", "4M76",
                 # Medium Difficulty
                "3R9A", "3S9D",
                 # Difficult
                "1E4K", "1EER", "1FAK", "1IRA", "2I9B", "3L89"]

# OX = Others, miscellaneous
dbd5_ox_list = [ # Rigid-body
                "1AK4", "1AKJ", "1EFN", "1EXB", "1FCC", "1FFW", "1GCQ", "1GPW",
                "1H9D", "1KLU", "1KXP", "1M27", "1OFU", "1QA9", "1RLB", "1S1Q",
                "1XD3", "1ZHI", "2A5T", "2B4J", "2BTF", "2HQS", "2VDB", "3BIW",
                "3BP8", "3D5S", "3H2V", "3P57",
                 # Medium Difficulty
                "1B6C", "1FC2", "1IB1", "1MQ8", "1N2C", "1SYX", "1XQS", "2CFH",
                "2HRK", "2OZA", "3AAA", "3AAD", "3BX7", "3DAW", "4JCV",
                 # Difficult
                "1ATN", "1DE4", "1H1V", "1RKE", "1Y64", "2C0L", "2J7P", "3AAD",
                "3F1P"]
# TODO: Re-add "3SZK" to medium difficulty (due to SASA calculation error)

# TODO: DUPLICATE 3P57
# TODO: EXCEPTION ON THE README

dbd5_all_list = dbd5_ei_list + dbd5_es_list + dbd5_er_list + dbd5_a_list + dbd5_ab_list + dbd5_og_list + dbd5_or_list + dbd5_ox_list
print(len(dbd5_all_list))
