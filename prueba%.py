n=int(input('Ingrese un numero: '))
descuento=n%10
r=n-descuento
d5=r%10
d4=(r//10)%10
d3=(r//100)%10
d2=(r//1000)%10     
d1=(r//10000)%10
print('las cifras del numero son: ', d1, d2, d3, d4, d5)
print('la suma de las cifras es: ', d1+d2+d3+d4+d5)

