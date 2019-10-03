http://rosalind.info/problems/fib/

rabArray = [1,1]

def getRabPairs(n,k):
    if n <= len(rabArray):
        return rabArray[n-1]
    else:
        temp_rab = getRabPairs(n-1,k) + (getRabPairs(n-2,k)*k)
        rabArray.append(temp_rab)
        return temp_rab

print(getRabPairs(34,2))
