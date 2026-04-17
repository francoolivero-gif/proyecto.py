try:
    n=int(input('ingrese un numero de 3 cifras: '))
    if n<=0:
        print('ingrese un numero mayor a 0')
    elif 99>n<999:
        print('ingrese un numero de 3 digitos')
except ValueError:
    print('ingrese un numero valido')
else:
    d3=n%10
    d1=(n//100)%10
    if d1==d3:
        print('el numero es capicua')
    else:        
        print('el numero no es capicua')
