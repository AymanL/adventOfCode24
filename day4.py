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
    newOrder = np.zeros
    for i in range(cote*2-1): #intuition
        if(i < cote):
            j = 0
            while j <= i:
                newOrder[i, j] = str(matrix[i-j,j])
                j += 1
        else:
            k = 0
            j = i - cote + 1
            maxLineIndex = 2*(cote-1) - i 
            while j < maxLineIndex:
                print("check", i, i-j, j)
                newOrder[i, k] = str(matrix[i - j, j])
                j += 1
                k += 1
            
    return newOrder

print(matrix)        
print(matrix_to_diagonal(matrix))
# test = np.zeros([4,1])
# print(test[1,0])
# print(test[0,1])
# total += matrix_count(matrix)
# matrix = matrix.transpose()
# total += matrix_count(matrix)

# print(b)
# print(matrix.shape[0]*)
# print(211 + 216)

