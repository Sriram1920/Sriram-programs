n=6
for i in range(1,n+1):
      for j in range(0,n-i+1):
        print(' ',end=' ')
      o=1
      for j in range(1,i+1):
         print(' ',o,sep=' ',end=' ')
         o=o*(i-j)//j
         print()
         
        
 
