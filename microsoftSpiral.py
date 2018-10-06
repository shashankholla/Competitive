# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:19:08 2018

@author: Shashank
"""
import sys
n = int(input())
C = int(input())
R = int(input())


c=n*n
x =int(n/2)+1
y = int(n/2)+1
t= 1
if ((y,x) == (R,C)):
   
    print(t)
else:
    
    for p in range(1,n):
        print("p is",p)
        if(p%2 != 0): 
            print("1L")
            for q in range(1,p+1):
                t = t+1
                x = x-1        
                y = y
                #print("X",x,"Y",y)
                if((x,y) == (C,R)):
                
                    print('E:',t)
                    sys.exit()
        
        
            for q in range(1,p+1):  
                t = t+1
                x = x        
                y = y + 1
                #print("X",x,"Y",y)
                if((x,y) == (C,R)):
                    print('E:',t)
                    sys.exit()
        if(p%2 ==0):
            print("2L")
            for q in range(1,p+1):
                t = t+1
                x = x+1    
                y = y
                #print("X",x,"Y",y)
                if((x,y) == (C,R)):
                    print('E:',t)
                    sys.exit()
            for q in range(1,p+1):  
                t=t+1
                x = x        
                y = y - 1
                #print("X",x,"Y",y)
                if((x,y) == (C,R)):
                    print('E:',t)
                    sys.exit()
    for q in range(1,n+1):
            t = t+1
            x = x-1        
            y = y
            #print("X",x,"Y",y)
            if((x,y) == (C,R)):
            
                print('E:',t)
                sys.exit()
           
        
