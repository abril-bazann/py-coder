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

#3ra función ejemplo de practica
#*args(se puede cambiar args por otro nombre pero siempre debe tener *)=varios argumentos desconocidos y sin valores definidos por defult. es como un diccionario, lista o tupla que se recorre
#**kwargs= cantidad de datos con datos por default
#siempre los primeros parámetros fijos, segundo los args, luego los kwags
def sumatoria(*lista_numeros):
    for number in lista_numeros:
        print(number)

sumatoria(1,2,3,4)

#4ta función ejemplo

def persona(**datos_personales):
    for dato_personal in datos_personales:
        print(f'{dato_personal} es {datos_personales[dato_personal]}', end=', ')

persona(nombre='Abril', apellido='Bazán', ciudad='Córdoba', pais='Argentina')
print('\n')
persona(nombre='Gonzalo', apellido='García', ciudad='Buenos Aires', pais='Argentina', edad=24, mascota=True)

#clases y objetos
class Perro: #init(método) se llama cuando creo un objeto de esa clase. es un constructor
  especie='Mamífero'
  def __init__(self, nombre, raza, edad):
    #atributos de instancia: lo que podría diferenciar a cada perro
    self.nombre=nombre #la clase Perro tiene un nombre
    self.raza=raza
    self.edad=edad

  def ladrar(self): #siempre pasar argumento. métodos definidos por el usuario
    print('GUAU, estoy ladrando!!!!!')
  def caminar(self, pasos):
    print(f'hola, soy {self.nombre} y estoy caminando {pasos} pasos')

  def __str__(self):
    return(f'hola, soy un perro y me llamo {self.nombre}')
#el __ 
#self siempre se pasa primero. 
perrito1=Perro("Kairo", "Ovejero", 7)
perrito2=Perro("Milo", "Labrador", 15)

print(f"Mi perrito se llama {perrito1.nombre} es de raza {perrito1.raza} y tiene {perrito1.edad} años ")
print(f"Mi perrito se llama {perrito2.nombre} es de raza {perrito2.raza} y tiene {perrito2.edad} años ")

perrito3=Perro('Peki', 'Pekines', 19)

print(perrito3.nombre)
print(perrito3.raza)
print(perrito3.edad) #acceder a atributos
print(perrito3.especie) #accedo a atributo de clase

#funciones creadas por usuario
perrito1.ladrar()
perrito2.ladrar()
perrito3.ladrar()
perrito1.caminar(22)

print(perrito1) 
#sin el __str__ imprime: <__main__.Perro object at 0x7f58988caf90>: objeto en tal direccion de memoria

class Persona:
  especie='humano' #atributos de clase
  caminar='bípedo'
  def __init__(self, nombre, apellido, edad, perro):
    #atributos de instancia: lo que podría diferenciar a cada perro
    self.nombre=nombre #la clase Perro tiene un nombre
    self.apellido=apellido
    self.edad=edad
    self.perro=perro

  def saludar(self): #siempre pasar argumento self
    return(f'hola! mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años')
  def __str__(self): #métodos especiales
    return(f'hola! mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años')
  def signo(self, signo):
    return(f'hola, soy {self.nombre} y mi signo es {signo}')
  def cumple(self):
    self.edad+=1
    return("WIIII estoy cumpliendo años") #no se debe imprimir solo aumentar la edad
  def estudiando(self):
    return('hola, estoy estudiando')
  def curso(self, materia):
    return(f'estoy en el mejor curso de {materia}')

#NO USAR PRINTS DENTRO DE UN MÉTODO. UTILIZAR RETURN. LUEGO IMPRIMIR AFUERA
persona1=Persona('Abril', 'Bazán', 19, perrito1)
print(persona1)
print(persona1.cumple())
print(persona1) #acá se suma 1 año en la edad
print(persona1.estudiando())
print(persona1.curso('python'))
print(persona1.signo('tauro'))
print(persona1.especie)
print(persona1.caminar)
print(persona1.perro)


#Posiblemente el segundo método más utilizado, con el que se crea una representación del objeto con significado para las personas. 



#otro método especial: len
'''
Podríamos usar la función len para obtener el número de elementos que tenga el objeto. 
Pero si probamos con el objeto nos encontraremos con un error.
Esto es así porque la clase no ha implementado aún el método __len__. Un problema se puede solucionar de tomar fácil al incluir este método.
'''