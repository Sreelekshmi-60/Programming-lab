string=input("Enter a string: ")
print("First character of entered string is ",string[0])
a=string[0]
print(a)
str1=string[1:]
for i in str1:
    if (i==a):
        str1=str1.replace(a,"$")
str1=a+str1
print(string,"is converted as ",str1)
