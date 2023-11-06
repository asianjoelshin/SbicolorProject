import argparse

parser = argparse.ArgumentParser(description='Separate the Sequences by Class')
parser.add_argument('-i', dest='input_file', type=str, help='Fasta Input File', required=True)
parser.add_argument('-o', dest='output_file', type=str, help='Output File', required=True)
args = parser.parse_args()

aminoacid_chart = {'A':'Ala','G':'Gly','I':'Ile','L':'Leu','P':'Pro','V':'Val',
                   'F':'Phe','W':'Trp','Y':'Tyr','D':'Asp','E':'Glu','R':'Arg','H':'His',
                   'K':'Lys','S':'Ser','T':'Thr','C':'Cys','M':'Met','N':'Asn','Q':'Gln'}

user_indices = []
run = True
while run:
    user_input = input('Enter the indexes based on your Weblogo coordinates or q to quit: ')
    if user_input == 'q' or user_input == 'Q':
        run = False
    elif user_input.isdigit():
        user_indices.append(int(user_input) - 1)
    else:
        print('Please enter either a coordinated number from Weblogo or q to quit')

class_id = []
title = True
while title:
    user_title_input = input('Enter the Class ID title: ')
    if user_title_input == '':
        print('Enter a Valid title')
    else:
        class_id.append(str(user_title_input))
        title = False

# Read muscle file and store as Dictonary: {Key (ID): Value (Amino Acid Sequence)}
muscle_file = {}
formula_list = []
def read_muscle_file(inputfile):
    with open(inputfile, 'r') as file:
        for i in file:
            id_sequence = i.strip().split('\t')
            id = id_sequence[0]
            sequence = id_sequence[1]
            muscle_file[id] = sequence
            formula_list.append(sequence)
    return muscle_file

def create_conserved_residues_line(user_indices):
    conserved_line = [' '] * len(list(muscle_file.values())[0])  
    for index in user_indices:
        conserved_line[index] = '*'
    return ''.join(conserved_line)

three_letter_code_users_aminoacid = []
def users_conserved_residues(formula_list, users_indices):
    users_aminoacid = []

    for i in users_indices:
        users_aminoacid.append((formula_list[0][i]))

    for i in users_aminoacid:
        for k, v in aminoacid_chart.items():
            if k == i:
                three_letter_code_users_aminoacid.append(v)
    return three_letter_code_users_aminoacid

separated_by_tab = {}
def read_and_replace_the_muscle(inputfile):
    with open(inputfile, 'r') as file1:
        for j in file1:
            gene_aminoacid = j.strip().split('\t')
            gene = gene_aminoacid[0]
            aminoacid = list(gene_aminoacid[1])
            #print(aminoacid)

            for indices in user_indices:
                aminoacid[indices] = '*'
                #print(aminoacid)

            aminoacid = ''.join(aminoacid)
            separated_by_tab[gene] = aminoacid
            #print(aminoacid)
    return separated_by_tab

def get_amino_acid_inbetween(aminoacid):
    aminoacid = aminoacid.replace('-','')
    amino_acid_inbetween = aminoacid.split('*')
    in_between_symbol_length = []
    formatted_table1 = []

    for in_between_symbol in amino_acid_inbetween:
        if in_between_symbol:
            length = len(in_between_symbol)
            in_between_symbol_length.append(length)

    for amino_acid_length in in_between_symbol_length:
        formatted_table1.append(f'{amino_acid_length}')

    formula = '-'.join(formatted_table1)
    #print(formula)
    return formula

inputfile = args.input_file
data = read_muscle_file(inputfile)
conserved_residues_line = create_conserved_residues_line(user_indices)
users_conserved_residues = users_conserved_residues(formula_list, user_indices)
data1 = read_and_replace_the_muscle(inputfile)

# outfile.write the sequences and the "Conserved Residues" line with asterisks
with open(args.output_file, 'w')as outfile:
    outfile.write('#' * 120 + '\n')
    outfile.write('\nYour Chosen Indices\n')
    outfile.write(f'{user_indices}')
    outfile.write('' + '\n')
    outfile.write('\nYour Metal Ligand Residues\n')
    outfile.write(f'{users_conserved_residues}\n')
    outfile.write('' + '\n')
    outfile.write('#' * 120 + '\n')
    for key, value in data.items():
        outfile.write('' + '\n')
        outfile.write(f'{value}\t{key}\n')
    outfile.write('' + '\n')
    outfile.write(f'{conserved_residues_line}\tConserved Residues\n')
    outfile.write('' + '\n')
    outfile.write('#' * 120 + '\n')

    formula_list = []
    int_formula_list = []
    output = []
    min_max_values = []
    final_output = []
    for gene, aminoacid in data1.items():
        formula = get_amino_acid_inbetween(aminoacid)
        outfile.write(f'\n{aminoacid}\t{gene}\t{formula}')
        outfile.write('' + '\n')
        formula_list.append([formula])
    outfile.write('\n')  
        
    for x in formula_list:
        #outfile.write(x)
        i = x[0].split('-')
        #outfile.write(i)
        int_formula = []
        for y in i:
            int_formula.append(int(y))
        int_formula_list.append(int_formula)

    num_rows = len(int_formula_list)
    num_cols = len(int_formula_list[0])

    for i in range(num_cols):
        new_row = []
        for j in range(num_rows):
            new_row.append(int_formula_list[j][i])
        output.append(new_row)

    for col in output:
        min_val = min(col)
        max_val = max(col)
        if min_val == max_val:
            min_max_values.append(f'({min_val})')
        else:
            min_max_values.append(f'({min_val}, {max_val})')

    for aminoacid_equation in range(len(min_max_values)):
        users_metal_ligand = three_letter_code_users_aminoacid[aminoacid_equation]
        value = min_max_values[aminoacid_equation]
        final_output.append(users_metal_ligand)
        final_output.append(value)
    final_output.append(three_letter_code_users_aminoacid[-1])

    metal_ligand_equation = '-'.join(final_output)
    outfile.write('#' * 120 + '\n')
    #outfile.write('' + '\n')
    #outfile.write(f'\nAmino Acids found between Metal Ligands:\n{formula_list}')
    #outfile.write('' + '\n')
    #outfile.write(f'\nSorted Amino Acids found between Metal Ligands by columns:\n{output}')
    #outfile.write('' + '\n')
    outfile.write(f'\nMatLab Equation:\n{class_id[0]}:\tN-{metal_ligand_equation}-C\n')
    outfile.write('' + '\n')
    outfile.write('#' * 120 + '\n')
    outfile.write('' + '\n')
