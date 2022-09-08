course=[("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")]
students=[("UGM2018001","Rohith Grewal"),("UGP2018132","Neha Talwar")]
tiples=[("UGM2018001","MA101","AB"),("UGP2018132","PH101","B"),("UGM2018001","PH101","B")]


lim=int(input("Enter the number of students to add: "))
mainlis=[]
for j in range(lim):
    rl=input("\nEnter the Roll Number: ")
    n=input("Enter the Name: ")
    lis=[]
    for i in range(0,1):
        c=input("Enter the Course Code: ")
        cn=input("Enter the Course Name: ")
        g=input("Enter the Grades: ")
        lis.append(c)
        lis.append(cn)
        lis.append(g)
    mainlis.append(rl)
    mainlis.append(n)
    mainlis.append(lis)
maintup=tuple(mainlis)
print(mainlis)
mainlis.sort()
print(mainlis)

    


