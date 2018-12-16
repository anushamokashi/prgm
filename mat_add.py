matrix1 = [[1, 2, 3],
	   [1, 5, 6],
	   [1, 1, 1]]
matrix2 = [[10, 11, 1],
	   [13, 1, 1],
	   [1, 1, 1]]
rmatrix = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]
print "gggg",(matrix1[1][0])

for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        rmatrix[i][j] = matrix1[i][j] + matrix2[i][j]

for r in rmatrix:
    print(r)




