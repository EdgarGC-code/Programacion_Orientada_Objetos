import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user = 'root',
        password = '',
        database = 'BD_Estudiantes'
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("Por el momento no es posible conectarse con la base de datos.... Intentelo mas tarde...")
    