
def graph(dnaArray, idArray):
    p = len(dnaArray[0])
    for j in range(0,len(dnaArray)):
        dnaString = dnaArray.pop(j)
        idString = idArray.pop(j)
        for x in range(0, len(dnaArray)):
            if dnaString[(p-3): p] == dnaArray[x][0:3]:
                print(idString, idArray[x])
        dnaArray.insert(j,dnaString)
        idArray.insert(j,idString)

dnaArray = ["TAAA", "AAATTTT", "TTTTCCC", "AAATCCC", "GGGTGGG"]
idArray = ["Rosalind_0498","Rosalind_2391","Rosalind_2323","Rosalind_0442", "Rosalind_5013"]




graph(dnaArray,idArray)
            
fh = open('/Users/saltside/Desktop/rosalind/rosalind_grph.txt','r')
line = fh.readline()
meta = ''
sequence = ''
x = 0 
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
    
