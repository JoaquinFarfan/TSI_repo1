def Primo(num):
    if num<2:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
num = int(input('Ingrese el numero que desea: '))
print('El numero ',num, 'es ',Primo(num))

