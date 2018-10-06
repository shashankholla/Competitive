def largestPermutation(k, arr):
    m = [0 for _ in range(n+1)]
    
    for u in range(n):
        m[arr[u]] = u
    #print(m)
    
    x = 0
    for l in range(k):
        #print("x is",x)
        while ( x < n and arr[x] >= n - x):
            
            x = x+1
        
        if x > n-1:
            break
        ind = m[n-x]
        arr[ind] = arr[x]
        m[n-x] = x
        m[arr[ind]] = ind
        arr[x] = n-x
        x = x+1
        #print(m,arr)
    
    return arr
f = open('input.txt','r')

nk = f.readline().split()

n = int(nk[0])

k = int(nk[1])

arr = list(map(int, f.readline().rstrip().split()))

a = largestPermutation(k, arr)
fptr = open('output.txt','w')
fptr.write(' '.join(map(str, a)))
fptr.write('\n')

fptr.close()


