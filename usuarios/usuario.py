from base import conexion as conn
from datetime import datetime 

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
        query = "insert into usuario values(null,%s,%s,%s,%s,%s) "
        datos = (self.nombre, self.apellido,self.correo,self.clave,fecha)

        try:
            cursor.execute(query,datos)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0,self]

        
        return result

    def identificar(self):
        pass

    git config --global user.email "you@example.com"
  git config --global user.name "Your Name"