#interfaz
#falta importar el modulo de aritm para el captcha
def bienvenida(): 
    print("¡Bienvenido a Tsundoku!") #Mensaje de Bievenidda


def menu(): #se crea un menú que tenga todas las opciones 
    print("\nMenu:")
    print("1. Registrame")
    print("2. Inicia sesión")
    print("3. Olvidé mi contraseña")
    print("4. Salir")

usuarios = {}  # Diccionario para almacenar usuarios

def registrar_usuario(): #opcion 1 para registrar el usuario
    print("\nRegistrar Usuario")
    nombre =  input("Ingrese su Nombre: ")
    apellido =  input("Ingrese su Apellido: ")
    dni = int(input("Ingrese su DNI: "))
    fecha_nacimiento = input("Ingrese Fecha de Nacimiento (aaaa/mm/dd): ")
    correo = input("Ingrese Correo Electrónico: ")
#falta: condiciones 
    while True: #condicion b: nombreUsuario debe tener entre 6 y 12 caracteres.
        nombre_usuario = input("Ingrese un nombre de Usuario: ")
        if nombre_usuario in usuarios:
            print("El nombre de usuario ya está registrado. Intenta con otro.")
        elif len(nombre_usuario) < 6 or len(nombre_usuario) > 12: #condicion b: nombreUsuario debe tener entre 6 y 12 caracteres.
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        else:
            break

#no se ejecuta porque me falta y no entiendo lo de buscar o iterar en lo ingresado 
    """while True:
        clave_ = input("Ingrese una Contraseña")
        if len(clave_) < 8:
            print("La clave debe tener al menos 8 caracteres")
        elif not (any for in clave_) and
                 (any for in clave_) and"""

#agregar mensaje de registro exitoso

def iniciar_sesion(): #no utilizar acentos!!!
    print("\nIniciar Sesión")
    nombre_usuario = input("Ingrese su Usuario: ")
    clave_ = input("Ingrese su Clave: ") #no utilizar contraseÑa por el caracter de la Ñ
 #agregar mensaje de ingreso exitoso

def olvido_clave():
   pass

if __name__ == "__main__":
    bienvenida()
    while True:
        menu()
        opcion = input("Selecciona una opción del menú: ")
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            olvido_clave()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")