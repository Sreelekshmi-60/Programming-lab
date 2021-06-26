def len_long(words):
    longest=words[0]
    length=len(words[0])
    for i in words:
        if(len(i)>length):
            longest=i
            length=len(i)
            print("Longest word is ",longest,"and its length is ",length)
list=[]
n=int(input("Enter number of words :"))
for i in range(n):
    word=input("Enter a word :")
    list.append(word)
len_long(list)    
