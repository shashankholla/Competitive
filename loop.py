import time

starttime = time.clock()

for i in range(1000):
    print(i)

print(time.clock() - starttime)

