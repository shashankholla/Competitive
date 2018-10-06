def pDay(year):
    if(year<1918):
        if(year % 4 == 0):
            return ('12.09.'+str(year))
        else:
            return ('13.09.'+str(year))#notleap
    
    
    if(year>1918):
        if((year % 400) ==0 or ((year % 4 == 0) and(year % 100 != 0))):
            return ('12.09.'+str(year))
        else:
            return ('13.09.'+str(year))
        
    
    
    if(year == 1918):
            print('26.09.1918')


if __name__ == "__main__":
    for i in range(1700,2701):
        print(pDay(i))