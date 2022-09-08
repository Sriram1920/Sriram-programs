

limit=int(input("Enter the Limit: "))
lis1=[]
for i in range(limit):
    x=int(input("Enter the Number: "))
    lis1.append(x)
even=[]
odd=[]

for i in lis1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Count even:",len(even))
print("Count Odd:",len(odd))
print("Sum Even:",sum(even))
print("Sum odd:",sum(odd))
