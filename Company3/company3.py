#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the functions below.
#

start_codon: str = "AUG"
stop_codon: str = "STOP"
#codon_to_amino_acid: Dict[str, str] = {
codon_to_amino_acid = {    
    "AUG": "Met",
    "CAA": "Gln",
    "CAG": "Gln",
    "GGU": "Gly",
    "GCG": "Ala",
    "UUU": "Phe",
    "UUC": "Phe",
    "UGG": "Trp",
    "UAA": stop_codon,
    "UAG": stop_codon,
    "UGA": stop_codon
}

def protein_synthesis_part_1(dna: str) -> str:
    # Assumptions: invalid if no start codon, no stop codon, invalid if any codon is not in the codon_to_amino_acid
    # dictionary
    mrna = dna.replace("T", "U")
    start_index = mrna.find(start_codon)
    result = []
    this_stop_codon = False
    if start_index == -1:
        return "INVALID"
    for i in range(start_index, len(mrna), 3):
        mrna_pair = mrna[i:i+3]
        if len(mrna_pair) < 3:
            break
        if mrna_pair in codon_to_amino_acid:
            if codon_to_amino_acid[mrna_pair] == stop_codon:
                this_stop_codon = True
                break
            else:
                result.append(codon_to_amino_acid[mrna_pair])
        else:
            return "INVALID"
    if result and this_stop_codon:
        return " ".join(result)
    else:
        return "INVALID"


def protein_synthesis_part_2(dna: str) -> str:
    # Assumptions: invalid if we don't have at least 3 exons, if we see an 'exon' with length % 3 != 0
    if not dna:
        return "INVALID"
    exons = ""
    for char in dna:
        if char == char.upper():
            exons += char
        else:
            exons += " "
    re.sub(' +', ' ', exons)
    exon_dna = exons.split(" ")
    for dnaitem in exon_dna:
        if len(dnaitem) % 3 != 0:
            exon_dna.remove(dnaitem)
    if len("".join(exon_dna)) < 9:
        return "INVALID"
    return(protein_synthesis_part_1("".join(exon_dna)))
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    part = int(input().strip())

    dna = input()

    if part == 1:
        result = protein_synthesis_part_1(dna)
    else:
        result = protein_synthesis_part_2(dna)

    fptr.write(result + '\n')

    fptr.close()
