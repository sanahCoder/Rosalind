#the probability of any parent producing offspring AaBb is 1/4

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def heterozygous(k,N):
    prob = 0
    for n in range (N, (2**k)+1):
        prob += ncr((2**k),n)*((1/4)**n)*((3/4)**(2**k - n))

    print(prob)


heterozygous(5,8)
