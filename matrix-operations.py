import numpy as np

#defining two matrizes
C = np.matrix(
    [
        [1, 1],
        [1, 1]
    ]
)

D = np.matrix(
    [
        [6, 2],
        [2, 6]
    ]
)

#defining basic matrix operations
addition=C+D
print('matrix addion: ')
print(addition)

subract=C-D
print('matrix subtraction: ')
print(subract)

multiplication=C*D
print('matrix multiplication: ')
print(multiplication)

invertMatrix=np.linalg.inv(D)
print('inverted matrix is: ')
print(invertMatrix)

#Determinant of a matrix
determinant=np.linalg.det(D)
print('determinant of matrix is: ')
print(determinant) 