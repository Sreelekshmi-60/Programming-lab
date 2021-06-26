integer=int(input("Enter an integer :"))
if integer<0:
    print("Please enter a positive integer!!")
else:
    fact=1
    for i in range(1,integer+1):
        fact=fact*i
    print("Factorial of ",integer,"is",fact)
    
