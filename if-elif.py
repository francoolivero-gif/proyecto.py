edad=int(input('ingrese su edad: '))
if edad<18:
    print('es menor de edad')
elif edad<27:
    print('es estudiante')
elif edad<60:
    print('es profesor')
else:
    print('es jubilado')