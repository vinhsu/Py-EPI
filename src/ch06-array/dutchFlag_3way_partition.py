'''
Created on Apr 30, 2016

@author: ninja
'''

def swap (a, x, y):
    a[y], a[x] = a[x], a[y]

def sort(A, lo, hi):
    if hi <= lo:
        return
    
    lt = lo
    gt = hi
    v = A[lo]
    i = lo+1
    while i <= gt:
        if A[i] < v:
            swap(A, lt, i)
            lt += 1
            i += 1
        elif  A[i] > v:
            swap(A, i, gt)
            gt -= 1
        else:
            i += 1
    
    sort(A, lo, lt-1);
    sort(A, gt+1, hi);
    
if __name__ == "__main__":
    A = [4,2,81,34,13,61,27,2,99,65,1,1,42,67,15,30,23,85,19]
    print ('origin=', A)
    sort(A, 0, len(A)-1)
    print ('result=', A)