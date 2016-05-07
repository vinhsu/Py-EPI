'''
Created on Mar 27, 2016

@author: ninja
'''
   
def addLastdigit(list):
    list.reverse()
    list[0] += 1;
    
    for i in range(len(list)):
        if list[i] == 10:
            list[i] = 0
            if (i+1 == len(list)):
                list.append(0)
            list[i+1] += 1
        
    list.reverse()
    return list

def main():
    l = [1,2,3,9,9]
    print("list=", l)
    res = addLastdigit(l)
    print("result=", res)

if __name__ == '__main__':
    main()