names=['Anu','Anoop','Jacob','Clara','Nandana']
count=0
for i in names:
    for j in i:
        if(j=='a'or j=='A'):
            count=count+1
print("Total number of 'a' in  the list is ",count)        
