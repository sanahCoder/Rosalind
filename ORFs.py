
http://rosalind.info/problems/orf/

DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon in DNA_CODON_TABLE.keys():
        protein = DNA_CODON_TABLE[codon]
    return protein


def reverse_complement(dna):
    comp = ''
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for c in reversed(dna):
        if c in lookup.keys():
            comp = comp + lookup[c]
    return comp


def possible_protein_strings(s):
    results = []
    indices = []

    l = len(s)
    for i in range(l):
        protein = translate_codon(s[i:i+3])
        if protein and protein == 'M':
            indices.append(i)

    for i in indices:
        found_stop = False
        protein_string = ''

        for j in range(i, l, 3):
            protein = translate_codon(s[j:j+3])

            if not protein:
                break

            if protein == 'Stop':
                found_stop = True
                break

            protein_string += protein

        if found_stop:
            results.append(protein_string)

    return results



small_dataset = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
fh = open('/Users/saltside/Desktop/rosalind/rosalind_orf.txt', 'r')
dnaArray = []
idArray = []

line = fh.readline()
meta = ''
sequence = ''
while line:
    line = line.rstrip('\n')
    if '>' in line:
        idArray.append(line[1:])
        if sequence != '':
           dnaArray.append(sequence)
        sequence = ''
    else:
        sequence = sequence + line
    line = fh.readline()

possible_a = possible_protein_strings(dnaArray[0])
possible_b = possible_protein_strings(reverse_complement(dnaArray[0]))
print("\n".join(set(possible_a + possible_b)))

