'''
Created on Mar 27, 2016

@author: ninja
'''
import max_diff

def maxTwoPair(list):
    res = max_diff.maxDiff(list)
    print('res=' , res)
    
    res2 = None
    if (res is not None):
        split = res[0][1]
        second = list[split+1:]
        print("\nsublist=")
        print(*second, sep=',')
        res2 = max_diff.maxDiff(second)
    
    max = res[1]
    if (res2 is not None):
        max += res2[1]
        print('res2=', res2)
        
    return max

if __name__ == '__main__':
    l = [17, 2, 52, 80, 111, 21, 100, 73, 45, 99]
    print("list=")
    print(*l, sep=',')
    result = maxTwoPair(l)
    print("\nthe max two pair=", result)
    