import numpy as np

#Get the text as a matrix
lines = np.loadtxt("datasets/day4.txt", dtype=str)
matrix = np.array([ list(word) for word in lines ])

def check_cross(firstCorner, secondCorner):
    return (firstCorner == "M" and secondCorner == "S") or (firstCorner == "S" and secondCorner == "M")


def check_surroundings(currentChar, upperLeft, upperRight, lowerLeft, lowerRight):
    if(check_cross(upperLeft, lowerRight) and check_cross(upperRight, lowerLeft)):
        return 1
    return 0

def count_xmas(inputMatrix):
    total = 0
    shape = inputMatrix.shape
    for i in range(shape[0]):
        if(i > 0 and i < shape[0] - 1):
            for j in range(shape[1]):
                if(j > 0 and j < shape[0] - 1):
                    if(inputMatrix[i,j] == "A"):
                        total += check_surroundings(
                            currentChar = inputMatrix[i,j],
                            upperLeft = inputMatrix[i-1,j-1],
                            upperRight = inputMatrix[i-1,j+1],
                            lowerLeft = inputMatrix[i+1,j-1],
                            lowerRight = inputMatrix[i+1,j+1]
                        )
    return total


print(count_xmas(matrix))