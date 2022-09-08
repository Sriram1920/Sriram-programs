import array 

time=int(input("Enter the Time Limit: "))

E=[]
L=[]
for i in range(1,time+1):
    print("Time:",i)
    e=int(input("No of Guests: "))
    l=int(input("No of Leaved: "))
    E.append(e)
    L.append(l)

enter=array.array('i',E)
leave=array.array('i',L)

x=int(input("Enter the Instance:"))
print("Max Guest at ",x,"th hour instance is:",enter[x-1]-leave[x-1])
