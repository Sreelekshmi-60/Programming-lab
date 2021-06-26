A=[3,2,5,1,11]
B=[0,2,4,6,8]
print("Length of first list :",len(A))
print("Length of second list :",len(B)) 
if len(A)==len(B):
    print("Lists are of same length")
else:
    print("Lists are of different length")
if sum(A)==sum(B):
    print("Lists have same sum and the sum is ",sum(A))
else:
    print("Lists have different sum and sum of A is",sum(A),"and sum of B is ",sum(B))
a=any(i in A for i in B)
if(a==1):
    print("A common value is present among lists")
else:
    print("No common value in the lists")
