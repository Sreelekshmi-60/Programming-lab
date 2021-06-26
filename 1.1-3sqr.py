a=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    a.append(int(input("Enter a number:")))
print("Squares of numbers in the list")
for i in a:
    print("Square of",i,"is",i*i)   
