def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transpose = []

    for column in range(columns):
        temp_row = []
        for row in range(rows):
            temp_row.append(matrix[row][column])
        transpose.append(temp_row)

    return transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(transpose(matrix))
