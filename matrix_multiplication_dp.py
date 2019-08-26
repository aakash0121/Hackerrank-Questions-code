# Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
# The problem is not actually to perform the multiplications, 
# but merely to decide in which order to perform the multiplications.

class Matrix(object):

    def __init__(self, matrix_dimension):
        self.md = matrix_dimension
        self.num_matrix = len(self.md)
        self.n = [[0]*self.num_matrix for x in range(self.num_matrix)]
    
    def matrix_multiplication(self):
        for l in range(2, self.num_matrix):
            for i in range(1, self.num_matrix - l + 1):
                j = i + l -1
                self.n[i][j] = float("inf")
                for k in range(i, j):
                    temp = self.n[i][k] + self.n[k+1][j] + self.md[i-1]*self.md[k]*self.md[j]
                    if temp < self.n[i][j]:
                        self.n[i][j] = temp
        print(self.n)
        
        return self.n[1][self.num_matrix-1]
    
if __name__ == "__main__":
    arr = [x for x in range(1,5)]

    matrix = Matrix(arr)
    print(matrix.matrix_multiplication())

