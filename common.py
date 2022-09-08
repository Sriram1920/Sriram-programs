

#Program to find the common values in two lists!

def listcommon(l1,l2):
    l=[]
    m=[]
    for i in l1:
        if i in l2:
            l.append(i)
    for o in l2:
        if  o in l1:
            m.append(o)
    print(l," & ",m)

l1=[2,7,5,3,4,1]
l2=[2,4,6,7,8,9]
print("\nGiven list is ",l1," & ",l2)
print("\nCommon Values are: ")
listcommon(l1,l2)
            
        
