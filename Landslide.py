numberOfCities = int(input())
city = dict()

for i in range(numberOfCities-1):
    inp = input().split(" ")
    print(inp)
    if(city.get(inp[0])):
        city[inp[0]].add(inp[1])
    else:
        city[inp[0]] = {inp[1]}
    if(city.get(inp[1])):
        city[inp[1]].add(inp[0])
    else:
        city[inp[1]] = {inp[0]}


instructions = int(input())

for i in range(instructions):
    command = input.split(" ")
    if command[0] == "q":
        print(distance(city,command[1],command[2]),0)


def distance(dc,a,b,c):
    if (b in dict[a].values):
        return c+1
    else if:
        for i in dict[a]:




print(city)
