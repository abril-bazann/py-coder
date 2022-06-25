import sys #modulo propio de python para usar cosas del sistema

#módulos y paquetes
'''
¿Qué es un script? Un script es un “guión” con instrucciones de código, (básicamente, lo que venimos haciendo hasta ahora) guardado con un nombre y ejecutado desde el intérprete (ide), estos scripts pueden tomar datos (argumentos) en el momento de la ejecución.
Pueden tomar estos datos desde el exterior y tener distintos comportamientos.
-------------
Los datos que se van a enviar se denominan argumentos, y son valores que se pasan al ejecutar un script para que este mismo después los modifique o haga lo que programemos con estos datos.

'''

print(sys.argv)
print(f'hola {sys.argv[1]}') #lista
#en terminal: python script2.py abril bazan = hola abril

#realizar un script que imprima una palabra una cantidad de veces pasada por parametro
#imprimir hola 5
if len(sys.argv) !=3:
    print('error, necesito dos argumentos')
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])

        #[nombrescript, parametro1(string), parametro2(numero int)]

'''
$ python script2.py abril 5
['script2.py', 'abril', '5']
hola abril (del ejemplo anterior)
abril
abril
abril
abril
abril
'''

