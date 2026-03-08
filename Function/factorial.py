
def factorial(n):
    s=1
    for i in range(1,n+1):

        s=s*n
        n -= 1
    return s

fact=factorial(4)
print(fact)
