import sys

def addition(num1, num2):
    add= num1 + num2
    return add
def subtraction(num1, num2):
    sub= num1 - num2
    return sub
def multiply(num1, num2):
    mul= num1 * num2
    return mul

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation== "add":
    output = addition(num1, num2)
    print(output)
if operation== "sub":
    output = subtraction(num1, num2)
    print(output)
if operation== "mul":
    output = multiply(num1, num2)
    print(output)