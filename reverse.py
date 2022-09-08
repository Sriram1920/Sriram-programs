

#Write the program to reverse a number:

num=input("Enter the Number: ")

if eval(num)<0:
    x=eval(num)*-1
    y=str(x)
    print('\nReverse number is  -'+y[::-1])
else:
    print("\nReverse value is",num[::-1])

