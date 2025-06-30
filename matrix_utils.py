def multiply_matrices(a, b):
    result = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += a[i][k] * b[k][j]
    return result

def multiply_matrix_by_number(matrix, number):
    return [[cell * number for cell in row] for row in matrix]