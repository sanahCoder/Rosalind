
    

def motifSearch(dnaArray1):

    
    bestMatch = ''
    n = 1
    flag = 0
    while n<= len(dnaArray1[0]):
        for x in range(0,(len(dnaArray1[0])-(n-1))):
            
            for j in range(1,len(dnaArray1)):
                
                if dnaArray1[j].find(dnaArray1[0][x:x+n]) == -1:
                    flag = 1
                
            if len(dnaArray1[0][x:x+n]) > len(bestMatch) and flag == 0:
                
                bestMatch = dnaArray1[0][x:x+n]
                break
            flag = 0
        n=n+1
    
    return bestMatch
    


dnaArray = []
idArray = []

fh = open('/Users/saltside/Desktop/rosalind/rosalind_lcsm.txt','r')
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
ind = 0
smallLen = len(dnaArray[0])
for x in range(1, len(dnaArray)):
    if smallLen > len(dnaArray[x]):
        smallLen = len(dnaArray[x])
        ind = x
    rem = dnaArray.pop(x)
    dnaArray.insert(0,rem)
                

print(motifSearch(dnaArray))

