#Programa principal desde la que se manda llamar los objetos de la clase de coches
# Importacion de clases
from coches import Coches

coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)

coche1.acelerar()
coche1.acelerar()

#print(coche1.__velocidad)
print(coche1.getVelocodad())

# coche1.__velocidad=400
print(coche1.setVelocidad())
# print(coche1.__velocidad)
