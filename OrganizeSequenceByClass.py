#Title: SbicolorProject - Sequencing By Class
#Graduate Student: Joel Shin
#PI: Dr. Yim

#Given: A FASTA File, whose description starts with '>'
#Return: An output file containing seperated sequences by Class ID

import argparse

parser = argparse.ArgumentParser(description='Seperate the Sequences by Class')
parser.add_argument('-i', dest = 'input_file', type = str, help = 'Fasta Input File', required = True)
parser.add_argument('-o', dest = 'output_file', type = str, help = 'Output File', required = True)
args = parser.parse_args()

#Input File Function
id_sequence = {}
def read_fasta(input_file):
    id = ''
    sequence = ''
    with open(input_file,'r') as file:
        for i in file:
            i = i.strip()
            if i.startswith('>'):
                if id != '':
                    id_sequence[id] = sequence
                id = i[0:]
                sequence = ''
            else:
                sequence += i
        if id != '':
            id_sequence[id] = sequence
    return id_sequence

#Sort the sequences
def sort(id_sequence):
    sorted_id_sequence = {}
    for k, v in id_sequence.items():
        if '.p_RING' in k:
            gene_id = k.split('.p_RING-')[1]
            sorted_id_sequence.setdefault(gene_id, []).append((k, v))
    return sorted_id_sequence

def write_class_sequence(sorted_id_sequence):
    with open(args.output_file, 'w') as output_file:
        for k, v in sorted_id_sequence.items():
            for x in v:
                output_file.write(f'{x[0]}\n{x[1]}\n')
            output_file.write('\n')
            print(f'Successfully written your {k} in {args.output_file}')
            print(id_sequence)
    
#Call Input file
fasta_file = args.input_file
data = read_fasta(fasta_file)
sorted_sequence = sort(data)
write_class_sequence(sorted_sequence)
