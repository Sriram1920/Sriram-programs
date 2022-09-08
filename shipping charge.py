

def items(x):
    s=750
    for i in range(x-1):
        s+=200
    print("Total charge of",x,"no of item is",s,"Rs")

i=int(input("Enter the Total number of items: "))
items(i)
