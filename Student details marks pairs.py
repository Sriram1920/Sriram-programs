

def studypairs(dic):
    key=[]
    for i in dic.keys():
        key.append(i)
    i=0
    main=[]
    key.sort()
    while key!=[]:
        l1=[]
        l1.append(dic[key[len(key)-1]])
        l1.append(dic[key[0]])

        key.pop(0)
        key.pop(len(key)-1)
        main.append(l1)
        i+=1
    return main

    
        
stud=int(input("Enter the Total students to enter: "))
if stud%2!=0:
    print("Odd number of students Cannot be made into Groups")
    exit()
mainlist=[]
dict1={}
for i in range(stud):
    student=[]
    name=input("\nEnter the Name: ")
    mark1=int(input("Enter the Physics Mark: "))
    mark2=int(input("Enter the Mathematics Marks: "))
    average=(mark1+mark2)/2
    student.append(name)
    student.append(average)
    dict1.setdefault(average,name)
    mainlist.append(student)

print(dict1)
print(studypairs(dict1))

