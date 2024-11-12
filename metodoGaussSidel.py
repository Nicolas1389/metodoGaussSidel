from math import*
from pprint import pprint

def distinf(x,y):
    return max([abs(x[i]-y[i]) for i in range (len(x))])
def GaussSeidel(A,b,x0, TOL, MAx):
    n= len(A)
    x=[0.0 for x in range(n)]
    k=1
    while k <=MAx:
        for i in range(n):
            if abs(A[i][i])<= 1e-15:
                print ("imposible de iterar")
                return
            s1= sum([A[i][j]*x[j] for j in range(i)])
            s2= sum([A[i][j]*x0[j] for j in range(i+1,n)])
            x[i]=(b[i]-float(s1)-float(s2))/float(A[i][i])
        pprint(x)
        if distinf(x,x0)<TOL:
            print (r"solución encontrada")
            return
        k+=1
        for i in range(n):
            x0[i]=x[i]
    print("iteraciones agotadas")
    return

A=[[1.7,8,6.2],[6.2,8.5,8.4],[6.6,1.7,5.6]]
b=[5.4,9,8.1]
x0=[6.6,9.5,8]
print("matriz A: \n")
pprint(A)
print()
print("vectro b: \n")
pprint(b)
print()
print("Semilla x0:  \n")
pprint(x0)
print("\n"+r"Iteración de Gauss-Seidel")
GaussSeidel(A,b,x0,1e-4,50)