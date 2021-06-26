n=int(input("Enter number of terms :"))
if n<=0:
    print("Please enter a positive integer!!")
elif n==1:
    print("Fibonacci series upto one is 0")
else:
    a=0
    b=1
    fib=0
    print("Fibonacci series upto ",n,"terms :",end=" ")
    for i in range(n):
        print(a,end=" ")
        fib=a+b
        a=b
        b=fib
        
    
