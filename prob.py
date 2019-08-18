import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def recessiveProb(k,m,n):
    homo = nCr(k,2)

    het2 = (3/4) * nCr(m,2)

    het = (1/2) * (m * n)

    hohet = k * m

    hoRec = k * n

    totComb = nCr((k + m + n), 2) 

    return ((homo + het + hohet + hoRec + het2)/totComb)

print(recessiveProb(23,27,30))


