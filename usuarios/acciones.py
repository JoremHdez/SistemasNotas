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
        try:
            correo = input("Ingresa tu email")
            clave = input("Ingresa una contraseña")
            
            usuario = user.Usuario("","",correo,clave)
            login = usuario.identificar()

            if correo == login[3]:
                print(f"Bienvenido usuario {login[1]}")
                self.proximasAcciones(login)


        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Datos incorrectos")
    
    def proximasAcciones(self,usuario):
        pass
