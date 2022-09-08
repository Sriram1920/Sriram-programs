a=[ ]
number = int (input () )
for i in range (1, number + 1):
    if number % i == 0:
        a.append(i)
print ( " the factors are:")
for i in a:
      print (i,end=" ")
      print ()

while 3:
    k=int (input ("enter which factor:"))
    if k<=len(a) :
         print (a [k-1] )
         break
    else:
        print ("enter correct value")
        
        
        
