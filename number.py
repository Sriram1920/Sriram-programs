number = int ( input (input (" please enter any number :"))) sum = 0
for i in range ( 1, number ):
      if (number % i == 0):
                sum = sum + i
      if (sum == number ):
          print ("\n % d is a perfect number " % number )
      else:
          print("\n % d is not a perfect number " % number )
  
