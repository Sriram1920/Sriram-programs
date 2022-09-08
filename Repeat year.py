def repeatyear(date):
    x=date%4
    if x==0:
        print(date+28)
    elif x==1:
        print(date+6)
    elif x==2 or x==3:
        print(date+11)

repeatyear(1947)
