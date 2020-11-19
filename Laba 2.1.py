adjacencyMatrix = [[0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
node = len(adjacencyMatrix)
rib, row = 0, 0
incidenceMatrix = [[0] * row for i in range(node)]


def PasteToArray(matrix, rowNumber, column, value):

	while len(matrix[rowNumber]) <= column:
		matrix[rowNumber].append(0)

	matrix[rowNumber][column] = value

for i in range(node):
	for j in range(i, node):
		if adjacencyMatrix[i][j] == 1:
			PasteToArray(incidenceMatrix, i, rib, 1)
			PasteToArray(incidenceMatrix, j, rib, 1)
			rib += 1

maxLength = 0

for i in range(node):
	if len(incidenceMatrix[i]) > maxLength:
		maxLength = len(incidenceMatrix[i])

for i in range(node):
	while len(incidenceMatrix[i]) < maxLength:
		incidenceMatrix[i].append(0)

for str in incidenceMatrix:
	print(str)