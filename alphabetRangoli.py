# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:15:41 2018

@author: Shashank
"""

def print_rangoli(size):
    
    for i in range(1,size+1):
        print('-'*int((4*size-3-1)/2-(4*i-4)),end="")
        
        for z in range(2*i-1):
            if(z<(i-1)):
                print(chr(97+size-z-1),end="")
            if(z>=(i-1)):
                print(chr(97+size+z-1),end="")
            if(z != i-1):
                print('-',end="")
        print('-'*int((4*size-3-1)/2-(4*i-4)))
              
              
             