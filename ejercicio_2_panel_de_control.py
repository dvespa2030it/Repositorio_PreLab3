# Panel de control del servidor

opcion = input("Bienvenido al panel de control del servidor. Por favor, seleccione una opción:\nA - Diagnóstico del sistema\nB - Sistema de enfriamiento de emergencia\nC - Registro de errores del servidor\nD - Apagar panel de control del servidor\n: ")

# Opciones del panel de control

match opcion:
    case "A":
        print("Iniciando diagnóstico del sistema...")
    case "B":
        print("Activando sistema de enfriamiento de emergencia del servidor...")
    case "C":
        print("Accediendo al registro de errores del servidor...")
    case "D":
        print("Apagando panel de control del servidor...")
    case _:
        print("Comando desconocido, Intente de nuevo")

# Validacion de la opción ingresada y retorno por comando desconocido
    
if opcion not in ["A", "B", "C", "D"]:
    print("Opción inválida. Por favor, seleccione una opción válida: A, B, C o D.")
    while opcion not in ["A", "B", "C", "D"]:
        opcion = input("Seleccione una opción válida: \nA - Diagnóstico del sistema\nB - Sistema de enfriamiento de emergencia\nC - Registro de errores del servidor\nD - Apagar panel de control del servidor\n: ")
        match opcion:
            case "A":
                print("Iniciando diagnóstico del sistema...")
            case "B":
                print("Activando sistema de enfriamiento de emergencia del servidor...")
            case "C":
                print("Accediendo al registro de errores del servidor...")
            case "D":
                print("Apagando panel de control del servidor...")
            case _:
                print("Comando desconocido, Intente de nuevo")