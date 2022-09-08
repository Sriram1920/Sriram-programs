


word = input("Enter the Word: ")
x=""
for i in word:
    if i not in 'AEIOUaeiou':
        x+=i
        
print(x)
