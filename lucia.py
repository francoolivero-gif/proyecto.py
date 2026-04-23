try:
    precio=int(input('ingrese el precio del producto: '))
except ValueError:
    print('Error: Por favor, ingrese un número válido para el precio.')
precio=int(input('ingrese el precio del producto: '))
b100=precio//100
precio=precio%100
b50=precio//50
precio=precio%50
b20=precio//20
precio=precio%20
b10=precio//10
precio=precio%10
b5=precio//5
precio=precio%5
b1=precio//1
precio=precio%1
print('la cantidad de billetes de 100 es: ', b100)
print('la cantidad de billetes de 50 es: ', b50)
print('la cantidad de billetes de 20 es: ', b20)
print('la cantidad de billetes de 10 es: ', b10)
print('la cantidad de billetes de 5 es: ', b5)
print('la cantidad de billetes de 1 es: ', b1)