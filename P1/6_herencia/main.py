#Programa principal desde la que se manda llamar los objetos de la clase de coches
# Importacion de clases
from coches import Coches, Camionetas, Camiones

coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)

camion1=Camiones("Dina", "negro", 2020, 180, 300, 12, 8, 2500)
camion2=Camiones("Star", "Banco", 2019, 150, 200, 14, 6, 2000)

camioneta1=Camionetas("Renault", "Amarillo", "2025", 240, 250, 8, "delantera", True)
camioneta2=Camionetas("Nissan", "Blanca", "2020", 180, 150, 6, "Tracera", False)




