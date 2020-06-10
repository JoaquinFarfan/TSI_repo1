# 1 kilogramo equivale a 2.2libras
# pide convertir desde 1 Kg hasta 199Kg 
def main():
    num1 = int(input('Ingrese primer kilogramo: '))
    num2 = int(input('Ingrese ultimo kilogramo: '))
    
    for n in range(num1,num2+1):
        print('Kilogramos','Libras')
        print('    ',n , '    ', round(n*2.2,1)) 
if __name__=='__main__':  
    main()

