cant_productos=int(input("Ingrese la cantidad de productos: "))
espacio=cant_productos//100
resto=cant_productos%100
if resto==0:
    print("El espacio necesario es: ",espacio*100)  
else:   
     print("El espacio necesario es: ",espacio*100+100)