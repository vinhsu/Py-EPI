'''
Created on May 20, 2016

@author: ninja
'''

def can_reach(A):
    lastReach = 0
    reach = 0
    for i in range(len(A)):
        print("i=", i, ", a[i]=", A[i])
        if (i > lastReach):
            if (lastReach == reach):
                return False
            else:
                lastReach = reach
        reach = max(reach, i + A[i])
    return True
        

def main():
    A = [3,3,1,0,2,0,1]
    print ("result=", can_reach(A))
    print("-------")
    B = [3,2,0,0,2,0,1]
    print ("result=", can_reach(B))
if __name__ == '__main__':
    main()