currentbalance=20000
atmchoice = int(input("1.with draw\n2.deposit\n3.balance enquiry\enter your choice between 1 to 3"))
if(atmchoice==1):
    drawamt=int(input("enter with draw amount:"))
    currentbalance=currentbalance-drawamt
    print("current balance:",currentbalance)
elif(atmchoice==2):
    deposit=int(input("enter deposit amount:"))
    currentbalance=currentbalance+deposit
    print("current balance:",currentbalance)
elif(atmchoice==3):
    print("current balance:",currentbalance)
else:
    print("invalid input\n enter your choice between 1 to 3")
    
    
