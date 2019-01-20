#Autor: Gbes
#Proyecto: Fractal generado por los movimientos de un caballo de ajedrez
#Idea: Hacer mallado 3^n*3^n colorear posiciones posibles del caballo.
from numpy import *
from pylab import *
from matplotlib import *
def F(x): #sistema de funciones iteradas
    f0 = x/5+[-1,2]
    f1 = x/5+[1,2]
    f2 = x/5+[2,1]
    f3 = x/5+[2,-1]
    f4 = x/5+[1,-2]
    f5 = x/5+[-1,-2]
    f6 = x/5 +[-2,-1]
    f7 = x/5+[-2,1]
    A = [f0,f1,f2,f3,f4,f5,f6,f7]
    return(A)
n = 1
coor = zeros((5**n,3))
X  = array([0])
Y = array([0])
Z = zeros(5**(n+1))
print(Z)
x = 2*5**(n-1)
for i in range(0,5**n): #Ejes coordenados
    er1 = array([i])
    for j in range(0,5**n):
        er2 = array([i,j,0])
        X = concatenate((X,er1), axis = 0)
        Y = concatenate((Y,er2), axis = 0)


#Generacion de posiciones posibles para el caballo para la primera iteración

print(coor)
nrows,ncols = 5**n, 5**n
X = delete(X,0,0)
Y = delete(Y,0,0)
k = size(Z)
for i in range (0,5**(n+1)):
        Z[i] = i
print(Z)
#Con la funcion reshape, acomodar los valores de Z en un mallado y pasar a imshow
grid = Z.reshape((nrows,ncols))
print(grid)
#imshow(grid,extent=(X.min(),X.max()+1,Y.min(),Y.max()+1),interpolation = "None", cmap="binary") #graficación
#show()
