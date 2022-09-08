age=int(input("enter your age:"))
if(age<=5):
    print("you are toddler")
elif(age<=12 and age>=6):
    print("you are kid")
elif(age<=19 and age>=13):
    print("you are teenager")
elif(age<=35 and age>=20):
    print("you are young")
elif(age<=60 and age>=36):
    print("you are middle age")
else:
    print("you are senior")
