import coches
import cochesBD

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("...¡Oprima cualquier tecla para continuar!...")

    def terminar(self):
        input(".... :::;: ¡GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n vuelva pronto! :::: ....")

    def opcionInvalida(self):
        input("\n\t.... ¡Opcion invalida, vuelve a intentarlo!.... ")

    def menu_acciones(self,tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::...\n")
        opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5. Salir \n \t\tElige una opción: ").lower().strip()
        return opcion

    def respuesta_sql(self,respuesta):
        if respuesta:
            input("\n\t...!Acción realizada con éxito!...")

    def datos_coche(self,tipo):
        self.borrarPantalla()
        print(f"\n\t...::: Ingresar los datos del {tipo} :::...\n")
        cochesito={}
        cochesito['marca']=input("\tIngresa la marca: ").upper().strip()
        cochesito['color']=input("\tIngresa el color: ").upper().strip()
        cochesito['modelo']=input("\tIngresa el modelo: ").strip()
        cochesito['velocidad']=input("\tIngresa la velocidad (Km/h): ").strip()
        cochesito['potencia']=input("\tIngresa la potencia (Hp): ").strip()
        cochesito['asientos']=input("\tIngresa el número de asientos: ").strip()
        return cochesito

    def menu_coches(self):
        opc=True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case '1':
                    # Crear objeto de coches y luego insertar BD.
                    cochesito=self.datos_coche("Coche")
                    coche1=coches.Coches(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    coches1=cochesBD.CochesBD(coche1.marca,coche1.color,coche1.modelo,coche1.velocidad,coche1.potencia,coche1.asientos)
                    respuesta=coches1.insertar()
                    self.respuesta_sql(respuesta)
                    del coches1
                    del coche1
                case '2':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del coche a eliminar: ").strip()
                    respuesta=cochesBD.CochesBD.eliminar(id)
                    self.respuesta_sql(respuesta)
                case '3':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del coche a actualizar: ").strip()
                    cochesito=self.datos_coche("Coche")
                    coche1=coches.Coches(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    coches1=cochesBD.CochesBD(coche1.marca,coche1.color,coche1.modelo,coche1.velocidad,coche1.potencia,coche1.asientos)
                    respuesta=coches1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coches1
                    del coche1
                case '4':
                    self.borrarPantalla()
                    registros=cochesBD.CochesBD.consultar()
                    num_coche=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\t Coche #: {num_coche}\n\t\tID: {fila[0]}\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]}\n\t\tVelocidad: {fila[4]}\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                        self.esperarTecla()
                    else:
                        print("...¡No se encontró información en la Base de Datos!... ")
                        self.esperarTecla()
                case '5':
                    opc=False
                case _:
                    self.opcionInvalida()

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL ::: \n\t1.- Coches\n\t2.-Salir\n\t Elige una opción: ").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coches()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion=False
                case _:
                    self.opcionInvalida()

if __name__=="__main__":
    apps=App()
