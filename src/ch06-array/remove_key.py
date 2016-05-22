'''
Created on May 21, 2016

@author: ninja

deleting repeated elements from a array
'''

def remove_key(key, A):
    wr = 0
    for i in range(len(A)):
        if (A[i] != key):
            A[wr] = A[i]           
            wr += 1 
    
    for j in range(wr, len(A)):
        A[j] = 0
    return A

def main():
    A = [2,35,5,5,17,11,15,54,13,5]
    R = remove_key(5, A)
    print ("result=", R)

if __name__ == '__main__':
    main()