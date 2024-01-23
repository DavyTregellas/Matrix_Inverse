# Finding the inverse of a 3x3 matrix

# Step1

matrix = [[6, 1, 4], [2, 7, 3], [5, 9, 8]]

determinantStep1 = matrix[2][0] * matrix[1][1] * matrix[0][2] + \
                   matrix[0][0] * matrix[2][1] * matrix[1][2] + matrix[1][0] * matrix[0][1] * matrix[2][2]

print(determinantStep1)

determinantStep2 = matrix[0][0] * matrix[1][1] * matrix[2][2] + \
                   matrix[1][0] * matrix[2][1] * matrix[0][2] + matrix[2][0] * matrix[0][1] * matrix[1][2]

print(determinantStep2)

determinant = determinantStep1 - determinantStep2

print("The determinant = ", determinant)

# Step2

row1_1 = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]

row1_1 = row1_1 * (-1)**2
#print(row1_1)
row1_2 = matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]

row1_2 = row1_2 * (-1)**3
#print(row1_2)
row1_3 = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]

row1_3 = row1_3 * (-1)**4
#print(row1_3)
row2_1 = matrix[0][1] * matrix[2][2] - matrix[2][1] * matrix[0][2]

row2_1 = row2_1 * (-1)**3
#print(row2_1)
row2_2 = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]

#print("check sum ", row2_2)
row2_2 = row2_2 * (-1)**4
#print(row2_2)
row2_3 = matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]

row2_3 = row2_3 * (-1)**5
#print(row2_3)
row3_1 = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]

row3_1 = row3_1 * (-1)**4
#print(row3_1)
row3_2 = matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]

row3_2 = row3_2 * (-1)**5
#print(row3_2)
row3_3 = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

row3_3 = row3_3 * (-1)**6
#print(row3_3)


# Step 3


matrixS2 = [[row1_1,row1_2,row1_3],[row2_1,row2_2,row2_3],[row3_1,row3_2,row3_3]]

print(matrixS2)

matrixS3 = [[row1_1,row2_1,row3_1],[row1_2,row2_2,row3_2],[row1_3,row2_3,row3_3]]

print(matrixS3)

for i in range(3):
    for j in range(3):
        matrixS3[i][j] = (1/determinant) * matrixS3[i][j]

print("\nThe Inverse Matrix: \n")
for row in matrixS3:
    print([format(element, ".2f") for element in row])
