
mylist = []
for i in range(1,101):
    mylist.append(i)

for j in mylist:
    if j%3 == 0:
        print("fizz")
    elif j%5 ==0:
        print("buzz")
    else:
        print(j)