def str_end(str2):
    if (len(str2)>=3):
        if(str2[-3:]=="ing"):
            str2=str2+"ly"
        else:
            str2=str2+"ing"
        print("Modified string is ",str2)
    else:
        print("Please enter a long word!!")
str1=input("Enter string :")
str_end(str1)
