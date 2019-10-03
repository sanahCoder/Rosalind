
http://rosalind.info/problems/gc/
def gc_content(dnaArray, idArray):
    max_content = 0
    max_id = 0
    for j in range(0,len(dnaArray)):
        gc_num = 0
        for nuc in dnaArray[j]:
            if nuc == 'G' or nuc == 'C':
                gc_num += 1
        perc = (gc_num/len(dnaArray[j]))*100
        if perc > max_content:
            max_content = perc
            max_id = idArray[j]
    return max_content, max_id


dnaArray = []

idArray = []



fh = open('/Users/saltside/Desktop/rosalind/rosalind_gc.fasta.txt','r')
line = fh.readline()
meta = ''
sequence = ''
x = 0 
while line:
    line = line.rstrip('\n')
    if '>' in line:
        idArray.append(line)
        if sequence != '':
           dnaArray.append(sequence)
        sequence = ''
    else:
        sequence = sequence + line
    line = fh.readline()

print(gc_content(dnaArray,idArray))
