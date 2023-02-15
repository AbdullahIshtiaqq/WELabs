def matrix_multiplication(m1, m2):
    resultantMatrix = []
    for i in range(len(m1)):
        rowResult = []
        for j in range(len(m2[0])):
            result = 0
            for k in range(len(m1[0])):
                result = result + m1[i][k]*m2[k][j]
            rowResult.append(result)
        resultantMatrix.append(rowResult)
    return resultantMatrix

row1 = int(input("Enter rows of first matrix: "))
col1 = int(input("Enter columns of first matrix: "))
row2 = int(input("Enter rows of second matrix: "))
col2 = int(input("Enter columns of second matrix: "))

if col1 == row2:
    matrix1 = []
    print("Enter values for 1st matrix..")
    for i in range(row1):
        rowList = []
        for j in range(col1):
            rowList.append(int(input(f'Enter value for row {i} and column {j}: ')))
        matrix1.append(rowList)

    matrix2 = []
    print("Enter values for 2nd matrix..")
    for i in range(row2):
        rowList = []
        for j in range(col2):
            rowList.append(int(input(f'Enter value for row {i} and column {j}: ')))
        matrix2.append(rowList)

    matrix = matrix_multiplication(matrix1,matrix2)
    print("\nThe resultant matrix after multiplication:")
    for i in range(len(matrix)):
        print(' '.join(map(str, matrix[i])))
else:
    print("Row and column must be equal for multiplication")
