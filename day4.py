import numpy as np
from scipy.ndimage import rotate

#Get the text as a matrix
lines = np.loadtxt("datasets/day4.txt", dtype=str)
matrix = np.array([ list(word) for word in lines ])

total = 0

#For a given line, look if XMAS or SAMX is found
def matrix_count(inputMatrix):
    matrixTotal = 0
    for line in inputMatrix:
        for i in range(len(line)-3):
            word = line[i] + line[i+1] + line[i+2] + line[i+3]
            if(word == 'XMAS' or word == 'SAMX'):
                matrixTotal += 1
    return matrixTotal

def matrix_to_diagonal(inputMatrix):
    cote = inputMatrix.shape[0]
    newOrder = np.full([cote*2-1, cote], "." ,dtype="S1")
    print(inputMatrix)
    for i in range(cote*2-1): #intuition
        if(i < cote):
            j = 0
            while j <= i:
                newOrder[i, j] = str(inputMatrix[i-j,j])
                j += 1
        else:
            k = 0
            j = i - cote + 1
            while j < cote:
                # print("check", i, i-j, j)
                newOrder[i, k] = str(inputMatrix[i - j, j])
                j += 1
                k += 1
    return newOrder

def numpy_cleaning(inputChar):
    return str(inputChar)[2]

def count_xmas(inputMatrix):
    total = 0
    transposed = inputMatrix.transpose()
    vectorized_char = np.vectorize(numpy_cleaning)
    diagonal_matrix = vectorized_char(matrix_to_diagonal(inputMatrix))
    print("sep")
    flipped_matrix = np.fliplr(inputMatrix)
    flipped_diagonal_matrix = vectorized_char(matrix_to_diagonal(flipped_matrix))

    total += matrix_count(inputMatrix)
    total += matrix_count(transposed)
    total += matrix_count(diagonal_matrix)
    total += matrix_count(flipped_diagonal_matrix)
    return total

print(count_xmas(matrix))

# print(np.full([10*2-1, 10], "." ,dtype="S1"))

# print(matrix_count(matrix))        
# print(matrix_to_diagonal(matrix))
# for i in range(10*2-1):
#     print(i)
# test = np.zeros([4,1])
# print(test[1,0])
# print(test[0,1])