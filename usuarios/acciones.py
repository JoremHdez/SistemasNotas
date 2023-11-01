from usuarios import usuario as user
class Acciones:

    def regristo(self):
        nombre = input("Ingresa tu nombre")
        apellido = input("Ingresa de tu apellido")
        correo = input("Ingresa tu email")
        clave = input("Ingresa una contraseña")
        
        usuario = user.Usuario(nombre,apellido,correo,clave)
        registrar = usuario.registrar()

        if registrar[0] >= 1:
            print("Registro exitoso")
        else:
            print("Regristo fallido")

    def login(self):
        correo = input("Ingresa tu email")
        clave = input("Ingresa una contraseña")