def exchange(string):
    string=string[-1]+string[1:-1]+string[0]
    return string
text=input("Enter a string :")
print("The entered string is ",text)
print("String after exchanging first and last character is ",exchange(text))
