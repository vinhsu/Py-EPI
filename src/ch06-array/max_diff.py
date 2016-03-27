'''
Created on Mar 27, 2016

@author: ninja
'''
   
def maxDiff(list):
    if len(list) < 2:
        return None
    
    max_diff = list[1] - list[0]
    min_element = list[0]
    min_idx = 0;
    maybe_min_idx = 0
    max_element = list[1]
    max_idx = 1
    for i in range(1, len(list)):
        if list[i] - min_element > max_diff:
            max_diff =  list[i] - min_element
            max_element = list[i]
            max_idx = i
            min_idx = maybe_min_idx
            
        if list[i] < min_element:
            min_element = list[i]
            maybe_min_idx = i
    
    t = (min_idx, max_idx)
    return [t, max_diff]

def main():
    l = [17, 2, 52, 80, 111, 21, 100, 73, 45, 99]
    print("list=")
    print(*l, sep=',')
    res = maxDiff(l)
    print("result=", res)
    

if __name__ == '__main__':
    main()