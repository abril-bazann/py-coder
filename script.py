print('hola mundo')

#after funciones
def recta(x):
    y = 2*x-1
    return y

resultado=recta(2)
print(f'el resultado de la funcion es {resultado}')
#el resultado de la funcion es 3

'''
definir variables:
num_1:float, num_2:float, resultado: float, opción deseada:str
definir procesos:
suma, resta, multiplicacion, division, saliir, control de errores...
definir el resultado:
devolver el resultado de cada operacion'''

def calculadora_amigable(opc, num_1,num_2):
    ''' calculadora de operaciones basicas
    parametros:
        opc--str:opcion del menú
        num_1--float: primer num a operar
        num_1--float: segundo num a operar
    retorno:
        resultado--str/float
    '''
    if opc.isdigit():
        opc=int(opc) #se renombra
        if opc==1:
            resultado=num_1+num_2
        elif opc==2:
            resultado=num_1-num_2
        elif opc==3:
            resultado=num_1*num_2
        elif opc==4:
            resultado=num_1/num_2
        elif opc==5:
            exit()
        else:
            resultado='la opcion ingresada es invalida'
    else:
        resultado='no se puede ejecutar, debe ingresar número'

    return resultado 


print('''
Menú
[1] Suma
[2] Resta
[3] Multiplicación
[4] División
[5] Salir
''')

opcion_deseada=input('Ingrese la opción que desea: ')
num_1=float(input('Ingrese el primer número: 1'))
num_2=float(input('Ingrese el segundo número: '))
calculadora_amigable(opcion_deseada, num_1, num_2)