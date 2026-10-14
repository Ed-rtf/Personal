A=[[],[],[]]
cofactor_matrix = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        input_value = int (input(f"Enter value for A[{i}][{j}]: "))
        A[i].append(input_value)
cofactor_matrix[0][0] = A[1][1]*A[2][2] - A[1][2]*A[2][1]
cofactor_matrix[0][1] = -(A[1][0]*A[2][2] - A[1][2]*A[2][0])
cofactor_matrix[0][2] = A[1][0]*A[2][1] - A[1][1]*A[2][0]
cofactor_matrix[1][0] = -(A[0][1]*A[2][2] - A[0][2]*A[2][1])
cofactor_matrix[1][1] = A[0][0]*A[2][2] - A[0][2]*A[2][0]
cofactor_matrix[1][2] = -(A[0][0]*A[2][1] - A[0][1]*A[2][0])
cofactor_matrix[2][0] = A[0][1]*A[1][2] - A[0][2]*A[1][1]
cofactor_matrix[2][1] = -(A[0][0]*A[1][2] - A[0][1]*A[1][0])
cofactor_matrix[2][2] = A[0][0]*A[1][1] - A[0][1]*A[1][0]
print("Cofactor Matrix:")
for row in cofactor_matrix:
    print(row)
transpose_matrix = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        transpose_matrix[i][j] = cofactor_matrix[j][i]
print("Transpose of Cofactor Matrix:")
for row in transpose_matrix:
    print(row)
determinant = A[0][0]*cofactor_matrix[0][0] + A[0][1]*cofactor_matrix[0][1] + A[0][2]*cofactor_matrix[0][2]
if determinant == 0:
    print("The matrix is singular and cannot be inverted.")
else:
    inverse_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            inverse_matrix[i][j] = transpose_matrix[i][j] / determinant
    print("Inverse Matrix:")
    for row in inverse_matrix:
        print(row)