
def get_matrix(n,m,value):       
    
    matrix_2 = []
    for i in range (n):
        matrix = []
        matrix_2.append(matrix)
        for j in range (m):
            matrix.append(value)
    return matrix_2
print(get_matrix(2,2,10))
print(get_matrix(3,5,42))
print(get_matrix(4,2,13))

