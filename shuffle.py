


def shuffle(l1,l2):
    main=[]
    if len(l1)>=len(l2):
        for i in range(len(l2)):
            main.append(l1[i])
            main.append(l2[i])
        for i in range(len(l2),len(l1)):
            main.append(l1[i])
    else:
        for i in range(len(l1)):
            main.append(l1[i])
            main.append(l2[i])
        for i in range(len(l1),len(l2)):
            main.append(l2[i])            
    return main

l1=[1,3,5,7,9,11,13,15,17,19,21,23,25,27]
l2=[2,4,6,8,10,12,14,16,18,20]
print(shuffle(l1,l2))
        
        
        
