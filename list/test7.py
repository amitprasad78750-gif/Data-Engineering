x = []
for i in range(1,50,2):
    x.append(i)
print(x)

x.insert(3,2)

for i in range(len(x)):
    if x[i] %2==0:
        print(f"this is even number  {x[i]}")
    else:
        print("this is odd number")
for i in range(len(x)):
    x.pop(i)
    print(f"the number is deleted in the list  {x[i]}")
print(x)