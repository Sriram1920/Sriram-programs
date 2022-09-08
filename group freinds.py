
#nUMBER OF GROUPS


n=int(input("Enter the total number of members in the group: "))
m=int(input("Enter the Number of Groups: "))
max_pairs=((n-m)*(n-m+1))/2
min_pairs=m*(((n-m)/m+1)*((n-1)/m))/2+((n-m)/(m))*((n-m)%m)

print("Minimum No of Pairs: ",int(min_pairs))
print("Maximum No of Pairs: ",int(max_pairs))
