#check if two list refer to the same object or not

def compare(l1,l2):
    l1.sort()
    l2.sort()
    if(l1==l2):
        print("the lists are containing the same objects ")
    else:
        print("the lists contin different objects ")

l1=[1,2,3,4,5]
l2=[5,4,3,2,1]
print("the first comparison is ",compare(l1,l2))
l3=['a','b','c','d']
l4=['d','b','c','a']
print("the second comparison is ",compare(l3,l4))


l4=[1,2,3,4,5,6]
l5=[1,2,3,4,5,6]
if (l4==l5):
    print("they are equal")
else:
    print("they are not equal ")
    

