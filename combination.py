num=list(input("Enter the 3 digit Number: "))
x=[]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j & j!=k & k!=i):
                print(num[i],num[j],num[k])
    
