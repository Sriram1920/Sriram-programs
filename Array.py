import array

def summes(x):
    l=[]
    for i in range(x):
        j=int(input("Enter the Value"))
        l.append(j)
    print("\nThe Given List is: ",l)
    x=array.array('i',l)
    m=max(x)
    n=min(x)
    print("max value is:",m,"Min value is :",n)
    print("sum =",m+n)
    print("difference=",m-n)

try:
    x=int(input("Enter the limit:"))
    if x<=0:
        print("Please Natural Numbers Only")
        exit()
    else:
        summes(x)
    
except:
    print("invalid Input")
