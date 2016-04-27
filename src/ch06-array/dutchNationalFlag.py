'''
Created on Apr 26, 2016

@author: ninja

Dutch National Flag Algorithm, or 3-way Partitioning
'''

def swap (a, x, y):
    a[y], a[x] = a[x], a[y]

def dutchNationalFlag(A):
    low = 0
    mid = 0
    hi = len(A)-1
    while mid <= hi:
        if A[mid] == 0:
            swap(A, low, mid)
            low += 1
            mid += 1
        elif  A[mid] == 1:
            mid += 1
        else:
            swap(A, mid, hi)
            hi -= 1
    print ('result=', A)

if __name__ == "__main__":
    A = [0,2,1,0,0,1,2,2,1,0,1,1,2,0,0,0,2,1,1]
    print ('origin=', A)
    dutchNationalFlag(A)