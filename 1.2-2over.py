integers=[]
n=int(input("Enter total number of elements :"))
for i in range(0,n):
    number=int(input("Enter a number:"))
    if number>100:
        integers.append("Over")
    else:
        integers.append(number)
print(integers)        
