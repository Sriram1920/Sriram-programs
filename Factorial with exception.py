
try:
    j=1
    val=int(input("Enter The Value: "))
    if val<0:
        print("Please Input any Positive Values")
    elif val==0 or val==1:
        print("Factorial is 1")
    else:
        for i in range(1,val+1):
            j*=i
        print("Factorial is:",j)
except:
    print("Please input a valid Positive Integer")
            
        
            
