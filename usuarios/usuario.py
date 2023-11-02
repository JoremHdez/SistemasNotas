from base import conexion as conn
from datetime import datetime 
import hashlib as has

conectar = conn.conexion()
database = conectar[0]
cursor = conectar[1]

class Usuario:
    def __init__(self,nombre,apellido,correo,clave):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave

    def registrar(self):
        fecha = datetime.now()
        #Cifrado contraseña
        cifrado = has.sha256()
        cifrado.update(self.clave.encode('utf8'))

        query = "insert into usuarios values(null,%s,%s,%s,%s,%s) "
        datos = (self.nombre, self.apellido,self.correo,cifrado.hexdigest(),fecha)

        try:
            cursor.execute(query,datos)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0,self]

        
        return result

    def identificar(self):
        query = "select * from usuarios where email = %s and clave = %s"
        #Cifrado contraseña
        cifrado = has.sha256()
        cifrado.update(self.clave.encode('utf8'))

        #DatoConsulta
        usuario = (self.correo,cifrado.hexdigest()) 

        cursor.execute(query,usuario)
        result = cursor.fetchone()

        return result
