x=int(input("Enter current year: "))
y=int(input("Enter last year: "))
while(x<=y):
    r=x%4
    if r==0:
      print(x)
    x=x+1   
