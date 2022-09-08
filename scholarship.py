marks_percentage=int(input("enter the marks percentage:"))
age=int(input("enter the age:"))
annual_income=int(input("enter the annual income:"))
if(marks_percentage>85):
    if(age<20):
        if(annual_income<200000):
            print("you are eligible for scholarship")
else:
    print("you are not eligible for scholarship")
 
