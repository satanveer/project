#how to define functions and all 
#def function(x,y):
#make a simple calculator using functions 





def sum(x,y):

    return x+y
def sub(x,y):
    
    return x-y
def mult(x,y):
    
    return x*y
def div(x,y):
    
    return x/y

num_input_1=int(input("enter the first number "))
num_input_2=int(input("enter the second number "))
choice=int(input("choose your program\n"\
    "1.Addition\n"\
        "2.Subtraction\n"\
            "3.Multiplication\n"\
                "4.Division\n"))
if choice==1:
    print("the sum is",sum(num_input_1,num_input_2))
elif choice==2:
    print("the subtraction is ",sum(num_input_1,num_input_2))
elif choice==3:
    print("the multiplication is ",mult(num_input_1,num_input_2))
elif choice==4:
    print("the division is ",div(num_input_1,num_input_2))


