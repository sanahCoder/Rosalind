
import string
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



def splice(dna, introns):
    for intron in introns:
        dna = remove_all(dna)



def remove_all(introns, string):
    index = 0
    for substr in introns: 
        length = len(substr)
        while string.find(substr) != -1:
            index = string.find(substr)
            string = string[0:index] + string[index+length:]
    return string

def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon in DNA_CODON_TABLE.keys():
        protein = DNA_CODON_TABLE[codon]
    return protein
def protein(seq):
    proteinStr = ''
    i = 0
    FindStop = False
    while FindStop == False:
        protein = translate_codon(seq[i:i+3])
        if protein != 'Stop':
            proteinStr = proteinStr + protein
            i = i + 3
        else:
            FindStop = True
    return proteinStr

fh = open('/Users/saltside/Desktop/rosalind/rosalind_splc.txt', 'r')
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

exons = remove_all(dnaArray[1:], dnaArray[0])
print(protein(exons))
