matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in matrix1:
    for j in i:
        print(j,end="\t")
    print()
print("-"*30)
matrix2 = [[i[0] for i in matrix1],[i[1] for i in matrix1],[i[2] for i in matrix1]]
for i in matrix2:
    for j in i:
        print(j,end="\t")
    print()
    
    
    
#chatgpt 
def interchange_rows_columns(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Create a new matrix with interchanged rows and columns
    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    
    # Interchange rows and columns
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

# Example usage
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]