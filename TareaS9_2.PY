def encontrar_primos(inicial, final):
    primos = []
    for n in range (inicial, final+1):
        contador = 0
        for i in range (1, n+1):
            if n % i == 0:
                contador += 1
        if contador == 2:
            primos.append(n)
    return primos
a = int(input('Ingresar rango inferior: '))
b = int(input('Ingresar rango superior: '))
print('Los números primos en el rango de ',a,'a ',b, 'son: ',encontrar_primos(a, b))