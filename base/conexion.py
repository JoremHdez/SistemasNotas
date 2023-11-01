import mysql.connector
#Hola
def conexion():
    try:
        database = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database ="notas",
            port = "3306"
        )

        cursor = database.cursor(buffered=True)

    except:
        print("Revisa los datos de la conexion")


    return [database,cursor]
    

