#simple calculator 
y=float(input("enter first number :"))
x=float(input("enter second number :")) 

print("1 add\n"\
    "2 subtraction\n"\
        "3 multiplication\n"\
            "4 division\n")

choice=int(input("CHOOSE YOUR OPERATION:"))

if choice==1:
    print("The sum of the numbers is:",x+y)
elif choice==2:
    print("The difference between the two is:",x-y)
elif choice==3:
    print("The product of the two is:",x*y)
elif choice==4:
    print("The division yields the result:",x/y)
else:
    print("invalid command")







        
    


