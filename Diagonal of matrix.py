

#Matrix Program

def matrix(columns,rows):
    matrix=[]
    for i in range(0,columns):
        row=[]
        for j in range(0,rows):
            inp=int(input("Enter the Row Value: "))
            row.append(inp)
        matrix.append(row)
    return matrix

def diagonal(mtx):
    print("The Diagonal 1 Values Are: ")
    for i in range(len(mtx)):
        print(mtx[i][i])
    print("The Diagonal 2 Values Are: ")
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            if ((i+j)==(len(mtx)-1)):
                print(mtx[i][j])
        

print("Only Input Square Matrix")        
rows=int(input("Enter the Number of Rows in the Matrix: "))
columns=int(input("Enter the Number of Columns in the matrix:"))

if  columns==rows:
    x=matrix(columns,rows)
    print("the input matrix is:",x)
    print()
    diagonal(x)
    
else:
    print("Their is no diagonal Value can only be attained from square matrix")
