from sympy import symbols
import numpy as np

# Creating symbols to use in equations
x1, x2, x3 = symbols('x1, x2, x3')

# defining a equation with one variable
y = x1**3 + 2*x2**4
print ('original equation: ')
print(y)

### first partial equations ###

# first derivation after x1
firstDerivationX1 = y.diff(x1)
print('the first derivation after x1 is: ')
print(firstDerivationX1)

# first derivation after x2
firstDerivationX2 = y.diff(x2)
print('the first derivation after x2 is: ')
print(firstDerivationX2)

### second partial equations ###

# second derivation after x1 x1
secondDerivationX1X1 = y.diff(x1, x1)
print('the second derivation after x1 x1 is: ')
print(secondDerivationX1X1)

# second derivation after x2 x2
secondDerivationX2X2 = y.diff(x2, x2)
print('the second derivation after x2 x2 is: ')
print(secondDerivationX2X2)

# second derivation after x1 x2
secondDerivationX1X2 = y.diff(x1, x2)
print('the second derivation after x1 x2 is: ')
print(secondDerivationX1X2)

# second derivation after x2 x1
secondDerivationX2X1 = y.diff(x2, x1)
print('the second derivation after x2 x1 is: ')
print(secondDerivationX2X1)

# constructing Hesse Matrix
hesseMatrix = np.matrix(
    [
        [secondDerivationX1X1, secondDerivationX1X2],
        [secondDerivationX2X1, secondDerivationX2X2]
    ]
)
print('the Hesse Matrix is: ')
print(hesseMatrix)
