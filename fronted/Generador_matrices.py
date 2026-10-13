n = 3 #numero temporal de el tamaño de la matrix n x n 
vert=["01","10","12","21"] #los conjuntos de vertices se tienen que representar como texto plano
mtx_B=[] #matrix vacia lista para ser rellenada


def Matrix_creator_(N):# generador basico de matrices nxn 
    for i in range(N):#ver como optimisar esto para tener un big o menor
        list=[]
        for j in range(N):
            list.append(0)
        mtx_B.append(list)    

def Matrix_fill(Matrix,Vert):# llenador basico de matrices nxn
    for v in Vert: # CAMBIO: antes decía "vertices" (no existía); ahora usa el parámetro Vert
        fila = int(v[0])
        columna = int(v[1])
        # CAMBIO: validación para evitar IndexError si el vértice no cabe en la matriz
        if fila < len(Matrix) and columna < len(Matrix):
            Matrix[fila][columna] = 1
        else:
            print(f"Aviso: el vértice {v} está fuera de la matriz")

#Black xhupalo
def Matrix_Mult(M1,M2):
    resultado = []
    for I in range (len(M1)):
        lista=[]
        for J in range(len(M2[0])):
            suma=0
            for K in range(len(M2)):
                suma+=M1[I][K]*M2[K][J]
            lista.append(suma)
        resultado.append(lista)
    return resultado

Matrix_creator_(n)
print(mtx_B)
print("\n")
Matrix_fill(mtx_B,vert)
print(mtx_B)
print("\n")

print(Matrix_Mult(mtx_B,mtx_B))