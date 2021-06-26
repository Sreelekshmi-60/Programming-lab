def wordcount(text):
    words=text.split()
    count=dict()
    for i in words:
        if i in count:
          count[i]=count[i]+1
        else:
           count[i]=1
    return count
x=input("Enter a line of text :")
print(wordcount(x))

