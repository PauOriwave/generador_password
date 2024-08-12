import random
import string

def generar_contrasena(longitud):
    # Define los caracteres permitidos (sin algunos símbolos)
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    
    # Genera la contraseña
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Solicitar al usuario la longitud de la contraseña
longitud = int(input("Ingrese la longitud deseada para la contraseña: "))

# Generar y mostrar la contraseña
contrasena_generada = generar_contrasena(longitud)
print("Contraseña generada:", contrasena_generada)