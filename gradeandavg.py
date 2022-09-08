m1=int(input("enter the mark: "))
m2=int(input("enter the mark: "))
m3=int(input("enter the mark: "))
m4=int(input("enter the mark: "))
total=m1+m2+m3+m4
avg=total/4
print(avg)
if avg>=90 and avg<=100:
    print("A Grade")
elif avg>=80 and avg<=89:
    print("B Grade")
elif avg>=70 and avg<=79:
    print("C Grade")
else:
    print("D Grade")
