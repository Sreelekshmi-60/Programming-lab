chardict={}
string=input("Enter a string :")
for i in string:
    keys=chardict.keys()
    if i in keys:
        chardict[i]=chardict[i]+1
    else:
        chardict[i]=1
print("Character frequency of letters =",chardict)        
