import math
def raiz_entera(n):
    y = math.sqrt(n)
    if y ** 2 == n:
        return True
    else:
        return False
n = int(input('Ingrese numero deseado: '))
print(raiz_entera(n))