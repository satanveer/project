#sum of first n squares
i=1
n=int(input("number upto which you want the sum for"))
sum=0
while(i<=n):
    sum=(i*i)+sum
    i=i+1
print(sum,"sum")