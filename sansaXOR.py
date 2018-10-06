#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
sumt = 0
def sansaXor(arr,i,j):
    global sumt
    
    sumx = 0
    
    
    for c in arr[i:i+j]:
            sumx = sumx ^ c
            
    sumt = sumt ^ sumx
    #print(arr[i:i+j],sumx,sumt)
    if j == n:
        return sumt
          
    if i+j == n:
            return sansaXor(arr,0,j+1)
    else:
        
            return sansaXor(arr,i+1,j)
sumt = 0
if __name__ == '__main__':
    
   

    t = int(input())

    for t_itr in range(t):
        sumt = 0
        n = int(input())

        arr = list(map(int, input().rstrip().split()))
        n = len(arr)
        result = sansaXor(arr,0,1)

        print(result)


