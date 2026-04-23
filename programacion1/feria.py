edad=int(input('ingrese su edad: '))
precio=150
if edad<4:
    print('el precio de la entrada es: ', 0)
elif edad<18:
    precioparamenores=precio/3
    print('el precio de la entrada es: ', precioparamenores)
elif edad<18:
    precioparamenos18=precio/2
    print('el precio de la entrada es: ', precioparamenos18)
elif edad<60:
    print('el precio de la entrada es: ', precio)
else:
    edad>=60
    precioparamayores=precio/3
    print('el precio de la entrada es: ', precioparamayores)