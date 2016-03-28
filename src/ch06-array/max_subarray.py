'''
Created on Mar 27, 2016

@author: ninja

Kadane’s Algorithm- Maximum subarray problem
'''

def maxSubArray(list):
    max_end_here = max_so_far = list[0]
    for i in range(1, len(list)):
        max_end_here = max(list[i], max_end_here + list[i])
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far

def maxSubArray2(list):
    max_end_here = max_so_far = list[0]
    begin = 0
    end = 0
    for i in range(1, len(list)):
        max_end_here += list[i]
        if (list[i] > max_end_here):
            max_end_here = list[i]
            begin = i
        if (max_so_far  < max_end_here):
            max_so_far = max_end_here
            end = i
    
    if begin > end:
        begin = end
        
    print('max sub=', list[begin:end+1])
    return max_so_far

if __name__ == '__main__':
    l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("list1=")
    print(*l, sep=',')    
    print("\nresult=", maxSubArray2(l))
    print("------")
    l = [7, -1, -3, -4, -1, 2, 1, -5, -4]
    print("list2=")
    print(*l, sep=',')    
    print("\nresult=", maxSubArray2(l))