'''
Created on Apr 20, 2016

The Buy-sale solution to get highest profit.

@author: ninja
'''
import random
from IN import INT64_MIN

def maxDifferenceKPairs(A, k):
    kSum = list()
    for i in range(k*2):
        kSum.append(float('-inf'))
    
    for i in range(len(A)):
        preKSum = list(kSum)
        sign = -1
        for j in range(len(kSum)):
            if j > i:
                break
            diff = sign * A[i] + (0 if j == 0 else preKSum[j - 1])
            kSum[j] = max(diff, preKSum[j])
            sign = sign * -1
    
    return kSum[len(kSum) - 1];

if __name__ == '__main__':
    n = 39; k = 4
    testA =list()
    
    for i in range(n):
        p = random.randint(0, 100)
        testA.append(p)
    
    print("testA=")
    print(*testA, sep=',')
    
    profit = maxDifferenceKPairs(testA, k)
    print("\nprofit=", profit)