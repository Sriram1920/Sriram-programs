
try:
    val=int(input("Enter The Value: "))
    c=0
    for i in range(2,val+1):
        if val%i==0:
            c+=1
    if c==1:
        print("Prime")
    else:
        print("Not Prime")
except:
    print("Please input a valid Positive Integer")
            
        
            
