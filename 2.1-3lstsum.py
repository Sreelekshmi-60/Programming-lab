listitem=[]
n=int(input("Enter number of elements in list :"))
for i in range(n):
    number=int(input("Enter a number into the list "))
    listitem.append(number)
print("The list is ",listitem)
listsum=0
for i in range(n):
    listsum=listsum+listitem[i]
print("Sum of elements in list =",listsum)    
