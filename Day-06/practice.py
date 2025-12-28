import sys

def sum():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    c = a + b
    print("the sum is: ",c)

sum()

def subtract(x,y):
    return x - y

result = subtract(10,5)
print("the difference is: ", result)


def multiply():
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    c = a * b
    print("the product is: ", c)

multiply()


def divide(x, y):
    return x / y

result = divide(20,4)
print("the quotient is: ", result)


x = int(input("enter value for x: "))
y = int(input("enter value for y: "))

if x > y and y < x:
    print("x is greater than y")
elif y > x and x < y: 
    print("y is greater than x")
elif x == y: 
    print("x is equal to y")
elif x != y and y != x:
    print("x is not equal to y")
else:
    print("invalid input") 

    
i = False
j = False

if i and j:
    print("both i and j are true") 
elif i or j: 
    print("either i or j is true") 
elif i and not j: 
    print("i is true and j is false")
else: 
    print("both i and j are false")

lst = list(input("enter names separated by space: ").split())
if "Sanjana" in lst: 
    print("Sanjana is present in the list")
elif "Rohan" not in lst: 
    print("Rohan is not present in the list")
else:
    print("invalid input")
