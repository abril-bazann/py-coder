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

#ecapsulamiento: atributo PRIVADO. __dos guiones bajos
class Persona:
    tipo = "Humano"  #Dato al que pueden acceder PUBLICO
    __sueldo = 2000  #No quiero que accedan a mi cuenta PRIVADO

    def __init__(self, nombre, apellido):
        self.nombre = nombre  #NO me molesta que sepan mi nombre  PUBLICO
        self.__apellido = apellido #No quiero que sepan mi apellido  PRIVADO

    def __soy_feliz(self):   #PRIVADO
        print("No les importa ¬¬")

    def edad(self):   #PUBLICO
        return 37 #Soy joven aún no miento con mi edad

persona1 = Persona("Fran", "Di Martino")

print(f"Resultado1: {persona1.tipo}\n")
#print(f"Resultado2: {persona1.__sueldo}\n")
print(f"Resultado3: {persona1.nombre}\n")
#print(f"Resultado4: {persona1.__apellido}\n")
#print(f"Resultado5: {persona1.__soy_feliz()}\n")
print(f"Resultado6: {persona1.edad()}\n")

#de afuera no se puede acceder

'''
¿Cómo encapsular correctamente?
Lo ideal es siempre dejar todo privado, y solo permitir que se pueda acceder y/o modificar los datos por medio de los métodos públicos get y set. Donde el programador es el que decide a qué se podra acceder y a que no, y principalmente que cosas se van a poder modificar o no desde afuera (FUNDAMENTAL).
get: todo datos
set: modifico datos
'''

class Jugador: #para acceder y devolver los atributos privados con métodos por FUERA   
    def __init__(self, nombre, apellido, perro, edad):

        #Se suelen hacer privados todos los atributos
         self.__nombre = nombre
         self.__apellido = apellido
         self.__perro=perro
         self.__edad=edad

    #Se generan metodos get PUBLICOS de los atributos 
    #que quieres que sean visibles.
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
    
    def get_perro(self):
        return self.__perro

    def get_edad(self):
        return self.__edad

    #Se generan metodos set PUBLICOS de los atributos 
    #que quieres que sean visibles y MODIFICABLES
    def set_nombre(self, nombre):
        print("estoy cambiando mi nombre, de manera correcta")
        self.__nombre = nombre

    def set_apellido(self, apellido):
        print("estoy cambiando mi apellido, de manera correcta")
        self.__apellido = apellido

    def set_perro(self, perro):
        print("estoy cambiando mi perro, de manera correcta")
        self.__perro = perro

    def set_edad(self, edad):
      if edad>0:
        self.__edad = edad #edad positiva no negativa tipo -20

jugador1 = Jugador("Brenda", "Benitez", perrito1, 21)
#gets de brenda
print(jugador1.get_apellido())  #Para acceder al apellido
print(jugador1.get_nombre())  #Para acceder al nombre()
print(jugador1.get_edad()) 
#sets para cambiar a ricardo
jugador1.set_apellido("Gutierrez")  #Para modificar al apellido
jugador1.set_nombre("Ricardo")  #Para acceder al nombre
jugador1.set_edad(29)
#gets de ricardo
print(jugador1.get_apellido())  #Para acceder al apellido
print(jugador1.get_nombre())  #Para acceder al nombre
print(jugador1.get_edad()) 
print(jugador1.get_perro().raza)



apellido_de_jugador_1=jugador1.get_apellido()
print(apellido_de_jugador_1)


#class Atleta
class Atleta:

 
  def __init__(self, nombre, apellido, altura, peso, telefono):
    
    self.__nombre = nombre
    self.__apellido = apellido
    self.__altura=altura
    self.__peso=peso
    self.telefono=telefono
    

 #método para que se imprima
  def __str__(self):
    return f"Atleta:  {self.__nombre}  {self.__apellido} "

  def mostrar(self):
    print(f"NOMBRE: {self.__nombre}\nAPELLIDO: {self.__apellido}\n")
    

  #Propios de la persona...

  #Creacion de getters y setters


  def getNombre(self):
    return self.__nombre

  def setNombre(self, nombreNuevo): #Modificar la edad :)
    self.__nombre=nombreNuevo

  def getApellido(self):
    return self.__apellido

  def setApellido(self, apellidoNuevo): #Modificar la edad :)
    self.__apellido=apellidoNuevo

  def getAltura(self):
    return self.__altura

  def setAltura(self, alturaNueva): #Modificar la edad :)
    self.__altura=alturaNueva

  def getPeso(self):
    return self.__peso

  def setPeso(self, pesoNuevo): #Modificar la edad :)
    self.__peso=pesoNuevo
  
  def getImc(self):
    imc= self.__peso/(self.__altura**2)
    if imc<18.5:
      return("Peso Inferior")
    elif imc<24.9:
      return("Normal")
    elif imc<29.9:
      return("Sobrepeso")
    elif imc<34.9:
      return("Obesidad")
    else:
      return("Obesidad Extrema")

p1 = Atleta("Fran", "Di Martino", 1.85, 93, 2804290162)
print(p1.getImc())
print(p1)  #Str
p1.mostrar()

#Herencias
class Persona:

    tipo = "Humano"  #Dato al que pueden acceder  PUBLICO
    

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  #NO me molesta que sepan mi nombre  PUBLICO
        self.__apellido = apellido #No quiero que sepan mi apellido  PRIVADO
        self.__edad=edad

    def __soy_feliz(self):   #PRIVADO
        print("No les importa ¬¬")

    def getEdad(self):   
        return self.__edad 
        
    def getApellido(self):   
        return self.__apellido

    def setApellido(self, apellidoNuevo):
      self.__apellido=apellidoNuevo

    def mostrar(self):
      print("Soy una persona")

#clase Empleado
class Empleado(Persona): #Sueldo, cargo

  #Atributos - constructor , las cosas del padre, las cosas del hijo
  def __init__(self, nomP, apeP, edadP, sue, car):
    #con el método super() llamo a mi clase Padre y debe tener este orden:
    super().__init__(nomP, apeP, edadP) #método de clases
    self.sueldo = sue
    self.cargo = car
    
  #def __str__(self):
      #return f"-----------> {self.sueldo} --- {self.cargo}"
  
  
  def mostrar(self):
      super().mostrar()
      print(f"SUELDO: {self.sueldo} --- CARGO: {self.cargo}")
  


  #Metodos

empleado1 = Empleado("Rodrigo", "Nicolau", 38, 1999.80, "Jefe")
empleado1.mostrar()
print(empleado1) #<__main__.Empleado object at 0x0000016B9CA4E5F0>

#Ejemplo integrador
class EmpleadoAdministrativo(Empleado):

  def __init__(self, nomP, apeP, edadP, sue, car, area):
    super().__init__(nomP, apeP, edadP, sue, car )
    self.area=area

  def mostrar(self):
    super(Empleado, self).mostrar()

adm=EmpleadoAdministrativo("fr","di",13,100,"sysadmin","info")
print(adm)

'''
Herencias Múltiples:
Hemos visto cómo se podía crear una clase padre que heredaba de una clase hija, pudiendo hacer uso de sus métodos y atributos. La herencia múltiple es similar, pero una clase hereda de varias clases padre en vez de una sola.
'''
