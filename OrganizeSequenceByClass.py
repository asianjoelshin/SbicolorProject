#!/usr/bin/env python
#Title: SbicolorProject - Sequencing By Class
#Graduate Student: Joel Shin
#PI: Dr. Yim

#Given: A Muscled Fasta file containing sequences for different Classes
#Return: An output file containing seperated sequences by Class

import argparse

parser = argparse.ArgumentParser(description='Seperate the Sequences by Class')
parser.add_argument('-i', dest = 'input_file', type = str, help = 'Fasta Input File', required = True)
parser.add_argument('-o', dest = 'output_file', type = str, help = 'Output File', required = True)
args = parser.parse_args()

id_sequence = {}
def read_fasta(input_file):
    """
    This Function will read your input file
    It will create a dictonary called 'id_Sequence' where the Key is the Gene ID and the value will store the sequence

    Return the ID and Sequece in form of a dictonary 
    """
    id = ''
    sequence = ''
    with open(input_file,'r') as fasta:
        for line in fasta:
            no_blanklines = line.strip()
            if no_blanklines.startswith('>'):
                if id != '':
                    id_sequence[id] = sequence
                id = no_blanklines[0:]
                sequence = ''
            else:
                sequence += no_blanklines
        if id != '':
            id_sequence[id] = sequence
    return id_sequence

def sort(id_sequence):
    """
    This Function will use the ID sequence dictonary as its input

    It will search for '.p_RING' in the Keys and split. Column one is anything after '-'

    The dictonary will change to sorted_id_sequence based on the class it is associated with
    """
    sorted_id_sequence = {}
    for id, sequence in id_sequence.items():
        if '.p_RING' in id:
            id_class = id.split('.p_RING-')[1]
            sorted_id_sequence.setdefault(id_class, []).append((id, sequence))
    return sorted_id_sequence

def write_class_sequence(sorted_id_sequence):
    """
    This Function will use the ID Sorted ID Sequence as its input

    The sorted_id_sequence should look like this:

    {YOUR_CLASS : [ID, Sequence]}

    Where the Key is the Class name and the value is a list of ID and sequence.

    If indexing the value, Column 0 is your ID and Column 1 is your sequence

    pep_file can also be used in same manner.
    """
    with open(args.output_file, 'w') as organizedFile:
        for geneClass, id_sequence in sorted_id_sequence.items():
            for id_sequence_list in id_sequence:
                organizedFile.write(f'{id_sequence_list[0]}\n{id_sequence_list[1]}\n')
            organizedFile.write('\n')
        print(f'Successfully written your organized {geneClass} in {args.output_file} file')

fasta_file = args.input_file
data = read_fasta(fasta_file)
sorted_sequence = sort(data)
write_class_sequence(sorted_sequence)
