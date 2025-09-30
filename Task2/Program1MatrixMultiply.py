# Function to multiply two matrices
def matrix_multiply(matA,matB):
    nrA=len(matA)
    ncA=len(matA[0])
    nrB=len(matB)
    ncB=len(matB[0])
    matC=[]
    if ncA!=nrB:
        print("Matrix cannot be multiplied.")

    else:
        for i in range(nrA):
            row=[]
            for j in range(ncB):
                c=0
                for k in range(nrB):
                    c+=matA[i][k]*matB[k][j]
                row.append(c)
            matC.append(row)
            

        print(matC)
                

    

# Lists to store matrix elements temporarily
listA=[]
listB=[]

# Input dimensions for Matrix A
rowA=int(input('Enter no. of rows in matrix A : '))
colA=int(input('Enter no. of columns in matrix A: '))


# Input elements for Matrix A
for i in range(rowA):
    row=[]
    for j in range(colA):
        ele=int(input("Enter element for row "+str(i+1)+" and column "+str(j+1)+":"))
        row.append(ele)
    listA.append(row)


# Input dimensions for Matrix B
rowB=int(input('Enter no. of rows in matrix B: '))
colB=int(input('Enter no. of columns in matrix B: '))

# Input elements for Matrix B
for i in range(rowB):
    row=[]
    for j in range(colB):
        ele=int(input("Enter element for row "+str(i+1)+" and column "+str(j+1)+":"))
        row.append(ele)
    listB.append(row)


# Call the function to multiply matrices
matrix_multiply(listA,listB)