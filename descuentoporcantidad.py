totalcamisetas=int(input('ingresar cantidad de camisetas: '))
valorcamisetas=totalcamisetas*8000
if totalcamisetas > 5:  
    descuento=valorcamisetas*0.25
    montofinal=valorcamisetas-descuento
else:
    montofinal=valorcamisetas
print('el monto final es: ',montofinal)
