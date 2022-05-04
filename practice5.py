i=1
n=int(input("enter the number to check if its prime or not "))
cpunt=0
while(i<=n):
    if(n%i==0):
        cpunt=cpunt+1
    i=i+1
if(cpunt==2):
    print("prime")
else:
    print("non prime")

