

x= int(input("Enter the Value: "))
i=2
lt=[]
while i<=x:
    if x%i==0:
        x=x//i
        lt.append(i)
    else:
        i+=1

print(lt)
lcm=1
i=2
while i<=max(lt):
    c=lt.count(i)
    print(c)
    if c%2==0:
        lcm*=((i**c)//2)
    else:
        lcm*=((i**c)//2)*i
    i+=1
print("LCM is: ",lcm)
        
    
    
    
        
               
               
    
