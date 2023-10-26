#!/usr/bin/env python
#Title: SbicolorProject - Align Sequences
#Graduate Student: Joel Shin
#PI: Dr. Yim

#Given: An Organized FASTA File
#Return: Aligned FASTA File using Muscle

from Bio.Align.Applications import MuscleCommandline
from io import StringIO
from Bio import AlignIO
import argparse

parser = argparse.ArgumentParser(description='Obtain the size (length) of each chromosome from the Genome File')
parser.add_argument('-i', dest='input_file', type=str, help='Genome Input File', required=True)
parser.add_argument('-o', dest='output_file', type=str, help='Output File', required=True)
args = parser.parse_args()
"""
This is a script that utilize the Bipython library. 

If you run into errors, likely you do not have Biopython installed

To install the Biopython library, in your terminal: pip install biopython
"""
ring = MuscleCommandline(input=args.input_file)
stdout, stderr = ring()

align = AlignIO.read(StringIO(stdout), 'fasta')

with open(args.output_file, 'w') as outputfile:
    for record in align:
        header = f'>{record.id}'
        sequence = str(record.seq)
        outputfile.write(f'{header}\t{sequence}\n')
        #outputfile.write(f'{header}\n{sequence}\n')    Activate this when wanting to create a Weblogo design
    print(f'Successfully saved your Muscled sequence as {args.output_file}')
