
#puck program


pk=list(input("Enter the Number: "))
rev=pk[::-1]
x=""
for i in rev:
    x+=i
    
if pk==rev:
    print(x,"is a Mirror Number")
else:
    print(x,"is not a Mirror Number")
