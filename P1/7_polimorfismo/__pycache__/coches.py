"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar un valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear el objeto y se manda llamar automaticamente al crearlo, es decir este metodo puede recibir parametros al momento de crear el objeto 

Cuando se crear un metodo constructor se utiliza la funcion _init_(), para que se llame automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.

El self es un parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.

No es necesario que tenga nombre self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función de la clase. Es decir por regla se utiliza en la palabra self pero puede ser llamado con otro nombre por ejemplo: valor, abd, parametro, etc.

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")
class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad+=1
        print(f"Ahora la velocidad es: {self._velocidad}")

    def frenar(self):
        self.__velocidad-=1
        print(f"Ahora la velocidad es: {self._velocidad}")

#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por   cada atributo que contenga la clase
        #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
        #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self,velocidad):
        self._velocidad=velocidad

    def getMarca(self):
        return self._marca

    def setMarca(self,marca):
        self._marca=marca

    def getColor(self):
            return self._color
    
    def setColor(self,color):
        self._color=color

    def getModelo(self):
            return self._modelo
    
    def setModelo(self,modelo):
        self._modelo=modelo

    def getPotencia(self):
                return self._potencia
        
    def setModelo(self,potencia):
        self._potencia=potencia

    def getAsientos(self):
                    return self._asientos
            
    def setModelo(self,asientos):
        self._asientos=asientos


class Camiones(Coches):
    def  __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    def carga(self, tipo_carga):
          print(f"El tioi de carga del camion es: {tipo_carga}")

    def acelerar(self):
            self._velocidad+=1
            print(f"Estoy acelerando como un camion: {self._velocidad}")
    
    def frenar(self):
        self.__velocidad-=1
        print(f"Estoy frenando como un camion: {self._velocidad}")

    def getEje(self):
          return self.__eje

    def setEje(self, eje):
          self.__eje = eje

    def getcapacidadCarga(self):
          return self.__capacidadCarga

    def setcapacidadCarga(self, capacidadCarga):
          self.__capacidadCarga = capacidadCarga


class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, traccion, cerrada):
        super().__ini__(marca, color, modelo, velocidad, potencia, asientos)
        self.__traccion=traccion
        self.__cerrada=cerrada

    def trasportar(self, num_pasajeros):
          print(f"El numero de pasajeros en la camioneta es: {num_pasajeros}")

    def acelerar(self):
            self._velocidad+=1
            print(f"Estoy acelerando como una camioneta: {self._velocidad}")
        
    def frenar(self):
        self.__velocidad-=1
        print(f"Estoy frenando como una canioneta: {self._velocidad}")

    def setTraccion(self, traccion):
        self.__traccion=traccion

    def getTraccion(self):
        return self.__traccion

    def getcerrada(self):
        return self.__cerrada   

    def setcerrada (self, cerrada):
        self.__cerrada =cerrada 
