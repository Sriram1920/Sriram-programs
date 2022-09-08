try:
    val=eval(input("Enter The Perfect Number to check: "))
    j=1
    sm=0
    if val<0:
        print("Please Enter a Positive Integer")
    else :
        for i in range(1,val):
            if val%i==0:
                sm+=i
        if sm==val:
            print(val,"is a Perfect Number")
        else:
            print(val,"is not a Perfect Number")

except:
    print("Only interger are to be entered ,float are not to be entered")
            
        
            
