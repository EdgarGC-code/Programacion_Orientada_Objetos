import estudiante

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

    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\t...::: Ingresar los datos del {tipo} :::...\n")
        estudiantito={}
        estudiantito['nombre']=input("\tIngresa el nombre: ").upper().strip()
        estudiantito['nota']=input("\tIngresa la nota (Calificación): ").strip()
        return estudiantito

    def menu_estudiantes(self):
        opc=True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Estudiante")
            match opc:
                case '1':
                    # Crear objeto de estudiante y luego insertar BD.
                    estudiantito=self.datos_estudiante("Estudiante")
                    estudiante1=estudiante.Estudiantes(estudiantito['nombre'],estudiantito['nota'])
                    respuesta=estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case '2':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del estudiante a eliminar: ").strip()
                    respuesta=estudiante.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                case '3':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del estudiante a actualizar: ").strip()
                    estudiantito=self.datos_estudiante("estudiante")
                    estudiante1=estudiante.Estudiantes(estudiantito['nombre'],estudiantito['nota'])
                    respuesta=estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case '4':
                    self.borrarPantalla()
                    registros=estudiante.Estudiantes.consultar()
                    num_estudiante=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\nEstudiante #: {num_estudiante}\n\tID: {fila[0]}\n\tNombre: {fila[1]}\n\tNota: {fila[2]}")
                            num_estudiante+=1
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
            opcion=input("\n\t\t ::: MENU PRINCIPAL ::: \n\t1.- estudiante\n\t2.-Salir\n\t Elige una opción: ").lower().strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opcion=False
                case _:
                    self.opcionInvalida()

if __name__=="__main__":
    apps=App()
