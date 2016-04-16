'''
Created on Apr 15, 2016

@author: ninja

same question as max_subarray
'''
from random import randint

def findMaximumSubarray(list):
    minSum = Sum = maxSum = 0
    for i in range(len(list)):
        Sum += list[i]
        if Sum < minSum:
            minSum = Sum
        if (Sum - minSum) > maxSum:
            maxSum = Sum - minSum
    return maxSum

if __name__ == '__main__':
    t = list()
    for i in range(100):
        t.append(randint(1,100))
    
    print(*t, sep=',')
    
    max = findMaximumSubarray(t)
    print('max=', max)