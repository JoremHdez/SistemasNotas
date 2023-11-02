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
        print("""
            1.Crear Notas
            2.Mostrar Notas 
            3.Eliminar Notas
            4.Salir

        """)

        opc = int(input("¿Qué quieres hacer?: "))
        if opc == 1:
            print("Crear")
            nombre = input("Titulo: ")
            print(nombre)
            self.proximasAcciones(usuario)

      
        elif opc == 2:
            print("Mostrar")
            self.proximasAcciones(usuario)

        elif opc == 3:
            print("Eliminar")
            self.proximasAcciones(usuario)
        
        elif opc == 4:
            print(f"Ok {usuario[1]}, hasta pronto")
            exit()
        
