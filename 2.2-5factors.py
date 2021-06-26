factors=[]
def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    print("List of factors of ",n," = ",factors)
num=int(input("Enter a number :"))
factor(num)
