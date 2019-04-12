import numpy as np

#defining a linear equation A=B with
#    4*x=8

A=np.matrix(
    [4,]
)

B=np.matrix(
    [8,]
)

x1=np.linalg.solve(A, B)
print('the solution is: x1=')
print(x1)


# defining a linear equation system C=D with
#   |  1*x1+2*x2=5  |
#   | 3*x1+3*x2=11  |

C=np.array(
    [
        [1,2],
        [3,4]
    ]
)

D=np.array(
    [6,13]
)

solution =np.linalg.solve(C, D)
print('the solution vector is: {x1, x2}=')
print(solution)
