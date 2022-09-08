class Error(Exception):
    pass
class CustomerError(Error):
    pass

try:
    main=[]
    def add():
        global main
        InsID=int(input("\nEnter the InsurenceID: "))
        name=input("Enter the Name: ")
        year=int(input("Enter the Number Of Years: "))
        main.append([InsID,name,year,amount])
    add()
    if main[0][0] not in customerslist:
        customerslist.pop(len(customerslist)-1)
        main.remove(main[0])
        raise CustomerError
except CustomerError:
    print("Employee is not in the Employee list: ")
    choice=input("Do you wish to add the Employee[Y/N]: ").lower()
    if choice=="y":
        add()
        customerslist.append(main[0][0])
print(customerslist)
print(main)
        
