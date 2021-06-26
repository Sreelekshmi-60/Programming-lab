from math import sqrt
digits=[]
n=int(input("Enter a range:"))
for i in range(n):
    number=int(input("Enter a four digit number "))
    count=0
    for j in str(number):
        rem=int(j)%2
        if rem==0:
            count=count+1
    if count==4:
      sqr=int(sqrt(number))
      if((sqr**2)==number):
         digits.append(number)
print("List of perfect squares with all digits even =",digits)        
