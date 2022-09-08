import random
def rand(a,b,c):
    rec=[]
    if(b>a):
        for i in range(c):
            rec.append(random.randint(a,b))
        return rec
    elif (a==b):
        print("A and B are equal so it will not be printed")
    elif(c<0):
        print("The Negative value will not be printed")
    else:
        print("B value should be greater than A")
a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
c=int(input("Enter number of elements:"))
print(rand(a,b,c))
    
