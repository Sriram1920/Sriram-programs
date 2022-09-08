l=[]
l1=[]
n=int(input('How much terms in first list :'))
n1=int(input('How much terms in second list :'))
for i in range(n):
    a=int(input('Enter a number :'))
    l.append(n)
    for j in range(n1):
        b=int(input('Enter a  2nd list number :'))
        l1.append(b)
print('1st list :',l)
print('2nd list :',l1)
d=l+l1
print('The merged list is :',d)
