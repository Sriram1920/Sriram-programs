
class Error(Exception):
    pass
class DateError(Error):
    pass

def season(month,date):
    if (month=="Dec" and date>=20) or month =="Jan" or month=="Feb" or (month=="Mar" and date<=20):
        print("its Summer Goin on Now!")
    elif (month=="Mar" and date>=20) or month =="Apr" or month=="May" or (month=="Jun" and date<=21):
        print("its Spring Goin on Now!")
    elif (month=="Jun" and date>=21) or month =="Jul" or month=="Aug" or (month=="Sep" and date<=22):
        print("its Autmn / Fall Goin on Now!")
    elif (month=="Sep" and date>=22) or month =="Oct" or month=="Nov" or (month=="Dec" and date<=21):
        print("its Winter Goin on Now!")
    else:
        print("Input a Valid Month")
print("\nMonths: ",['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

x=input("Enter The 3 letters of Month: ")
l=x.lower()
m=l.capitalize()

if m  not in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
    print("Wrong Month please re-enter")
    exit()
        
try:
    month=m
    date=int(input("Enter the date: "))
    if month in ['Jan','Mar','May','Jul','Aug','Oct','Dec']:
        if date<=31 and date>0:
            season(month,date)
        else:
            raise DateError
    elif month=="Feb" and date<=28 and date>0:
        season(month,date)
    elif month in ['Apr','Jun','Sep','Nov']:
        if date<=30 and date>0:
            season(month,date)
        else:
            raise DateError
    else:
        raise DateError

except DateError:
    print("You are so stupid! Please Give the Correct date atleast")

