import math 
def factorial(x):
    factorial = math.factorial(x)
    return factorial
x = int(input('Ingrese un numero entero: '))
print('El factorial de ',x,' es',factorial(x))