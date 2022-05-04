#calculator using functions 
def sum(x,y):
    return x+y

def sub(x,y):
    return x-y
1
def mult(x,y):
    return x*y

def div(x,y):
    return x/y

choice=input("Choose 1,2,3,4-->")
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if choice == "1":
    print("the sum of the numbers is",sum(num1,num2))
elif choice =="2":
    print("the subtraction of the two numbers is ",sub(num1,num2))
elif choice=="3":
    print("the multiplication of the two numbers is ",mult(num1,num2))
elif choice=="4":
    print("the division of the two numbers is ",div(num1,num2))
else:
    print("invalid argument")


