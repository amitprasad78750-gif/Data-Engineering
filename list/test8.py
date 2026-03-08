
numchar = []
for i in range(1,10):
    numchar.append(i)
print(numchar)
newlst=[i**2 for i in range(1,len(numchar)+1)]
print(newlst)