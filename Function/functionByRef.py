
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

"""Add the above function in dictionary where key = '+','-','*','/' """
operation= {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
         }
"""TODO : use dictionary operation to perform the operation """

#print(operation["*"](5,3))
num1 = int(input("What is the first number?:  "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = int(input("what is the second number?:  "))

print(operation[operation_symbol](num1,num2))
