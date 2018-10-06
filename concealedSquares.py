import math
import time



def checkSuccess(x,number):
    
    for i in range(2,l,2):
        if(int(x[i]) != int(number[i])):
          
            
            return False
            
    return True
    





a = int(input())
b = input().strip("").replace(" ","")

number = int("0".join(b))

start = int(math.sqrt(number))-1

startsq = start ** 2

initDiff = start*2 - 1

flag = True

strnumber = str(number)
l = len(strnumber)



start_time = time.time()
while(flag):
    #print(startsq)
    if(not checkSuccess(str(startsq),strnumber)):
        initDiff +=2
        startsq +=initDiff
        start +=1
        
    else:
        flag = False

print(time.time() - start_time)
    
print(start)
        
    
    








