from usuarios import acciones as acc

print("""
      
    Acciones Disponibles
      1.-Registro
      2.-Login

""")

accion = acc.Acciones()

opc = int(input("¿Qué quieres hacer?: "))
if opc == 1:
    print("Ingresa los datos para poder ser registrado")
    accion.regristo()

elif opc == 2:
    print("Ingresa tu usuario y contraseña para poder ingresar")
    accion.login()