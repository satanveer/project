#check whether a given number is 0,+ve,-ve
a=int(input("Enter your number :"))
if a>0:
    print("The number is positive ")
elif a<0:
    print("The number is negative ")
else:
    print("The number is Zero ")

#write a program to check if it is between 1-10 then also determine if it is even or odd 
x=int(input("Enter your number to test if it is between 1-10 and is even or odd"))
if x>0 and x<=10:
    print("The number is between 1 to 10 ")
    if x%2==0:
        print("The number is even ")
    else:
        print("The number is odd")
else:
    print("The number is not between 1 to 10 ")

#program to check if a number is prime or not 
y=int(input("Enter the number to check if it is prime or not "))
if y>1:
 for i in range(2,y):
     if y%i==0:
         print("the number is not prime ")
         break
 else:
    print("the number is prime ")
else:
    print("the number is not prime ")



    
