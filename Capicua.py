def capicua(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
num = int(input('Ingrese el numero deseado: '))
print('El numero ',num,' es',capicua(num))