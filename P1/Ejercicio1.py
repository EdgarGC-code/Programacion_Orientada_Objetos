print("\033c")
class Alumnos:
    _nombre = ""
    _edad = 0
    _calificacion = 0.0

    def mostrarDatos(self,nombre,edad,calificacion):
        print(f"Nombre: {nombre} \nedad: {edad} \ncalificacion: {calificacion}")

    def estaAprovado(self, calificaciones):
        if calificaciones > 7:
            return "Esta aprovado"
        else:
            return "No esta aprovado"

alumno1=Alumnos()
Alumno2=Alumnos()

alumno1.mostrarDatos("Edgar", 23, 9.2)
