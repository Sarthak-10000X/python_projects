#Making a simple calculator!
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
print("===SIMPLE CALCULATOR===")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
choose=int(input("Choose number from 1 to 4 to perform following task: "))
a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
try:
 if choose==1:
    print(f"{a} + {b} = {add(a,b)}")
 elif choose==2:
    print(f"{a} - {b} = {substract(a,b)}")
 elif choose==3:
    print(f"{a} * {b} = {multiplication(a,b)}")
 elif choose==4:
    print(f"{a} / {b} = {division(a,b)}")
except ValueError:
   print("INVALID NUMBER")




