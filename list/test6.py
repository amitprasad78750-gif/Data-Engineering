
print("Please enter the number for the star print")
n=int(input())
for j in range(n):
    for i in range(j):
        print("*  ",end="")
    n=n-1
    print()
