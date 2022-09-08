

#Scenario based questions!
#SLOT 1

def sumsquare(l):
    x=[]
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even+=(i**2)
        else:
            odd+=(i**2)
    x.append(odd)
    x.append(even)
    return "list of odd even is:",x

x= int(input("Enter the limit:"))
lis=[]
for i in range(x):
    l= int(input("Enter the value: "))
    lis.append(l)
           
if lis==[]:
    print("Empty List")
else:
    print(sumsquare(lis))
            
        
            
