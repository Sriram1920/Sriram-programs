

def Zahid(n):
    x=1
    if n<0:
        return False
    elif n==1 or n==0:
        return 1
    else:
        for i in range(1,n+1):
            x*=i
        return x


line=int(input("Enter the Total Length Of the Triangle: "))

for i in range(line):
    for j in range(line-i+1):
        print(end=" ")
    for j in range(i+1):
        print((Zahid(i))//(Zahid(j)*Zahid(i-j)),end=" ")
    print()
        
