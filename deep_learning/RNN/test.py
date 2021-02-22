from common.Np import *

x = np.array([[1,2,3],[4,5,6],[7,8,9]])

t = np.array([[0,0,1],[1,0,0],[0,1,0]])

z = t.argmax(axis=1)

print(x[np.arange(3), z])

print(x[[2,0,1],[0,0,0]])