#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, a):
    i = k - 1
    t = 0
    count = 0
    l = []

    for i in range(n):
        if a[i] == 1:
            l.append(i)
    c = len(l)
    while(i < c):
        if l[i] < k - 1:
            c += 1
            count = 1
    if count  == 0:
        return -1
    i += 1
    while(i < c):
        if l[i] 

    




    while(i < n):
        if a[i] == 1:
            #print("Counting. i -> ",i)
            count += 1
            t = i
            if i + 2*k - 1 < n:
                i += 2*k - 1
            else:
                if i + k - 1 >= n -1:
                    return count
                else:
                    i = n-1
        else:
            while(a[i] != 1 and (i > t + k or (count == 0 and i >= 0))):
                print("Inside while", i)
                i -= 1
            if not (i > t + k or (count == 0 and i >= 0)):
                return -1
            
    return count
                
        
        
        
        
        
    
    
    
    

if __name__ == '__main__':
   
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    print(pylons(k, arr))

   