def main():
    m=int(input("INGRESE EL NUMERO DE FILAS: "))
    n=int(input("INGRESE EL NUMERO DE COLUMNAS: "))

    M=[]

    for i in range(m):
        M.append([0]*n)
    
    for i in range(m):
        for j in range(n):
            M[i][j]=int(input("M["+str(i)+";"+str(j)+"]: "))
    
    cadena=""
    for i in range(m):
        for j in range(n):
            cadena=cadena+"\t"+str(M[i][j])
        cadena=cadena+"\n"

    print(cadena)



if __name__ == "__main__":
    main()