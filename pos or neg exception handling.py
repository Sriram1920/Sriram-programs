
try:
    val=int(input("Enter Thet Number to check: "))
    if val<0:
        print("Negative Number")
    elif val==0:
        print("Neither Negative Nor Positive")
    else:
        print("Postive Number")

except:
    print("Please input a valid Positive Integer")
            
        
            
