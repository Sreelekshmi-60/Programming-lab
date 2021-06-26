x=input("Enter a string: ")
print("Given word is :",x)
y=['A','E','I','O','U','a','e','i','o','u']
print("Vowels in the word :")
for i in x:
  for j in y:
    if i==j:
       print(i)
