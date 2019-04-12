import numpy as np

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

e=6
f=4
g=e+f
print('e+f=')
print(g)

h=C+D
print ('matrix addion: ')
print(h)

subract=C-D
print ('matrix subtraction: ')
print(subract)

multiplication=C*D
print ('matrix multiplication: ')
print(multiplication)

invertMatrix=np.linalg.inv(D)
print ('inverted matrix is: ')
print(invertMatrix)

A = [
        [2, 2],
        [3, 3]
    ]

B = [
        [2, 2],
        [3, 3]
    ]

print(A)
print(B)
print(A+B)