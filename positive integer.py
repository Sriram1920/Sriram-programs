def primeproduct(m):
    l=[]    
    if m>=2:
        for i in range(2,m):
            if m%i==0:                
                l+=[i]            
        if len(l)==2:
            if m==l[0]*l[1]:
                if l[1]%l[0]==0:
                    return False
                return True
        elif len(l)==1:
            if m==l[0]*l[0]:
                return True
        else:
            return False     
    else:
        return False
