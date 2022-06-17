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

#creando funcion
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
        try:
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
        except ZeroDivisionError:
            resultado='el segundo número ingresado es cero, por lo que la division da error'
    else:
        resultado='no se puede ejecutar, debe ingresar número en la opción'

    return resultado 
# Main code

#mostrando menú
print('''
Menú
[1] Suma
[2] Resta
[3] Multiplicación
[4] División
[5] Salir
''')

#solicitando números
try:
    opcion_deseada=input('Ingrese la opción que desea: ')
    num_1=float(input('Ingrese el primer número: '))
    num_2=float(input('Ingrese el segundo número: '))
except ValueError:
    resultado='la sintaxis del codigo es incorrecta'
    
#llamando función
resultado_operacion=calculadora_amigable(opcion_deseada, num_1, num_2)
print(resultado_operacion)