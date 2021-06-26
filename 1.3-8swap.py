def swap(x,y):
    str1=y[0]+x[1:]
    str2=x[0]+y[1:]
    return str1+" "+str2
a=input("Enter first string :")
b=input("Enter second string :")
print("After swapping the characters at first position of two strings,the new string will be ",swap(a,b))
