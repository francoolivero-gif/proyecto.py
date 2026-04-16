try:
    comida=int(input('Ingrese el precio de la comida: '))
    bebida_sa=int(input('Ingrese el precio de la bebida sin alcohol: '))
    bebida_ca=int(input('Ingrese el precio de la bebida con alcohol: '))
    invitados=int(input('Ingrese el numero de invitados: '))
    invitados_ca=int(input('Ingrese el numero de invitados que consumiran bebida con alcohol: '))
    importe=comida/invitados+bebida_sa/invitados
    try:
        extra=bebida_ca/invitados_ca
    except ZeroDivisionError:
        extra=0
        print('No hay invitados que consuman bebida con alcohol, por lo tanto no se cobrara un extra por este concepto')
    else:
        print('El extra por bebida con alcohol es de: ', extra) 
    print('El importe total por persona es de: ', importe) 
except ValueError:
    print('los datos ingresados son erroneos.'
        '\npor favor vuvlva a intentarlo con datos numericos')


                     
