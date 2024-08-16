apellido = input("Ingrese su Apellido: ")
nombre = input("Ingrese su Nombre: ")

def crear_usuario_automatico(nombre, apellido):
    primer_apellido = apellido.split()[0] 
    inicial_nombre = nombre[0] 
    username = inicial_nombre + primer_apellido
    username = username.capitalize()
    return username

mostra = crear_usuario_automatico (nombre , apellido)
print(f"su usuario es: {mostra}")
clave= input("ingrese su contraseña: ")
confirmar_contrasena = input("Confirme la contraseña: ")    
if clave == confirmar_contrasena:  
    print ("Contraseñas coinciden")
    print ("clave generada con exito.")
else:
         print ("Las Contraseñas no Coinciden")




