numbers=[]
even=[]
limit=int(input("Enter the number of elements in list :"))
for i in range(limit):
    element=int(input("Enter number into list :"))
    numbers.append(element)
    if element%2==0:
        even.append(element)
print("List of numbers entered : ",numbers)
print("List of even numbers :",even)
        
