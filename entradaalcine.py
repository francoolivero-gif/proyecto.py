totalentradas=int(input('ingresar cantidad de entradas'))
costototal=totalentradas*3500
if totalentradas > 2:
    descuento=costototal*0.2
    preciofinal=costototal-descuento
else:
    preciofinal=costototal
print('el precio final es: ',preciofinal)